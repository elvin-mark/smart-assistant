import requests
import numpy as np
from typing import Any, List, Mapping, Optional
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from langchain_core.embeddings import Embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
import faiss
from langchain.chains import RetrievalQA
import streamlit as st
from io import StringIO

class CustomEmbeddings(Embeddings):

    def __init__(self, endpoint: str="http://localhost:8282/embedding"):
        self.endpoint = endpoint
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        res = requests.post(self.endpoint,json={
            "content":texts
        })
        return np.concat([np.array(e["embedding"]) for e in res.json()])

    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]


class CustomLLM(LLM):
    endpoint: str = "http://localhost:8181/completion"
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        payload = {"prompt": prompt,"n_predict": 128}
        try:
            response = requests.post(self.endpoint, json=payload)
            response.raise_for_status()
            return response.json().get("content", "No response from server.")
        except requests.RequestException as e:
            return f"Error: {e}"


    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"endpoint": self.endpoint}

    @property
    def _llm_type(self) -> str:
        return "custom"

embeddings = CustomEmbeddings()

index = faiss.IndexFlatL2(384)
db = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

llm = CustomLLM()

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever()
)

def upload_file(data: str):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150,length_function=len,is_separator_regex=False)
    docs = text_splitter.create_documents([data])
    db.add_documents(docs)

def get_response(prompt:str) -> str:
    return qa.invoke(prompt)["result"]


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    upload_file(stringio.read())

st.title("Chat with the Smart Assistant!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What would you like to know?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = get_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

audio_value = st.audio_input("Record a voice message")
if audio_value:
    st.audio(audio_value)
import requests
import numpy as np
from typing import Any, List, Mapping, Optional
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from langchain_core.embeddings import Embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import streamlit as st

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
        """Return custom parameters (if needed)."""
        return {"endpoint": self.endpoint}

    @property
    def _llm_type(self) -> str:
        """Get the type of language model used by this chat model. Used for logging purposes only."""
        return "custom"

with open("/home/elvin/Downloads/quantum.txt", "r") as f:
    data = f.read()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150,length_function=len,is_separator_regex=False)
docs = text_splitter.create_documents([data])

embeddings = CustomEmbeddings()
db = FAISS.from_documents(docs, embeddings)
llm = CustomLLM()

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever()
)

def get_response(prompt:str) -> str:
    return qa.invoke(prompt)["result"]

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
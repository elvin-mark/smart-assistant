import os
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


def process_audio(data: Any):
    res = requests.post("http://localhost:8080/inference",files={
        "file": ("audio.wav",data.read())
    })
    return res.json().get("text","")
    
def generate_speech(text: str):
    command = f'espeak-ng -w tmp/spoken.wav "{text}"'
    os.system(command)
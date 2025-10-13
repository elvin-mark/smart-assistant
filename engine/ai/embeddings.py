from langchain_core.embeddings import Embeddings
import requests
import numpy as np
from typing import List
from engine.config import EMBEDDINGS_ENDPOINT


class CustomEmbeddings(Embeddings):

    def __init__(self, endpoint: str = EMBEDDINGS_ENDPOINT):
        self.endpoint = endpoint

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        res = requests.post(self.endpoint, json={"content": texts})
        return np.concat([np.array(e["embedding"]) for e in res.json()])

    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]


embeddings = CustomEmbeddings()

from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
import faiss
from langchain_text_splitters import RecursiveCharacterTextSplitter
from engine.ai.embeddings import embeddings
from engine.ai.llm import llm
from langchain.chains import RetrievalQA

index = faiss.IndexFlatL2(384)
db = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=db.as_retriever()
)


def upload_file(data: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len,
        is_separator_regex=False,
    )
    docs = text_splitter.create_documents([data])
    db.add_documents(docs)


def get_response(prompt: str) -> str:
    return qa.invoke(prompt)["result"]

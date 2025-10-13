from langchain.tools import tool
from engine.ai.rag import document_qa


@tool("document_qa", return_direct=True)
def get_response_from_documents(prompt: str):
    """Response to the question of the user based on the documents that has been uploaded it

    Args:
        prompt: question input by the user
    """
    return document_qa.invoke(prompt)["result"]

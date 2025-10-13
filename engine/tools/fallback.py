from langchain.tools import tool
from engine.ai.llm import short_answers_llm

@tool("llm_fallback", return_direct=True)
def llm_fallback(query: str) -> str:
    """Use this tool when no other tool is relevant; answer using your own knowledge."""
    # This will be handled internally by the LLM agent itself, so just a placeholder
    return short_answers_llm.invoke(query).content
from langchain_openai import ChatOpenAI
from engine.config import LLM_ENDPOINT
from engine.config import LLM_API_KEY

llm = ChatOpenAI(
    base_url=LLM_ENDPOINT,
    api_key=LLM_API_KEY,
    model="model_name",
    temperature=0.8,
    timeout=60,
    max_retries=2,
)

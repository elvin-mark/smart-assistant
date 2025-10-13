from langchain_openai import ChatOpenAI
from engine.config import LLM_ENDPOINT, LLM_API_KEY, LLM_TYPE
from langchain_google_genai import ChatGoogleGenerativeAI

if LLM_TYPE == "local":
    llm = ChatOpenAI(
        base_url=LLM_ENDPOINT,
        api_key=LLM_API_KEY,
        model="model_name",
        temperature=0.8,
        timeout=60,
        max_retries=2,
    )

elif LLM_TYPE == "google":
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

else:
    raise Exception(f"no valid LLM: {LLM_TYPE}")

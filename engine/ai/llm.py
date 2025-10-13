from langchain_openai import ChatOpenAI
from engine.config import LLM_ENDPOINT, LLM_API_KEY, LLM_TYPE
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

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

system_prompt = (
    "You are a helpful and concise assistant. "
    "Your sole purpose is to provide direct, very short, and factual answers. "
    "Do not include any conversational filler, explanations, or introductory/closing remarks."
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
short_answers_llm = prompt_template | llm

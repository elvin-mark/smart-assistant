from langchain.agents import create_agent
from engine.tools import tools
from engine.ai.llm import llm

agent = create_agent(
    model=llm,
    tools=tools
)

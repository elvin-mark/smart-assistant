from langchain.agents import initialize_agent, AgentType
from engine.tools import tools
from engine.ai.llm import llm

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3
)

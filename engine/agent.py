from langchain.agents import initialize_agent, AgentType
from engine.tools.calculator import calculator
from engine.tools.document_qa import get_response_from_documents
from engine.ai.llm import llm

tools = [calculator, get_response_from_documents]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3
)

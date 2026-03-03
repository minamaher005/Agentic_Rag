# app/services/query.py
from langchain_core.messages import HumanMessage
from app.graph.builder import graph


def ask(question: str) -> str:
    """Run a question through the agent graph and return the final answer."""
    result = graph.invoke({"messages": [HumanMessage(content=question)]})
    return result["messages"][-1].content
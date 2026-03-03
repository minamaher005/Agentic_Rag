## create agent state
from typing import Sequence, Annotated
from pydantic import BaseModel
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class agentstate(BaseModel):
    """agent state model"""
    messages: Annotated[Sequence[BaseMessage], add_messages]
import os
from pydantic import BaseModel
from app.infrastructure.llm import model
from app.tools.retriever_tools import technicalretrievar, healthretriever_tool
from app.tools.arxiv_tool import arxiv
from app.tools.tavily_tool import tavily
from app.core.state import agentstate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage
from typing import Literal
from langchain_core.prompts import PromptTemplate
from pydantic import Field
## the start node
def agent(state:agentstate):
    """
    Invokes the agent model to generate a response based on the current state. Given
    the question, it will decide to retrieve using the retriever tool, or simply end.
    Args:
        state (messages): The current state
    Returns:
        dict: The updated state with the agent response appended to messages
    """
    print("---CALL AGENT---")
    messages = state.messages
    llm = model.bind_tools([technicalretrievar, healthretriever_tool, arxiv, tavily])
    response = llm.invoke(messages)
    return {"messages": [response]}


## the generate node

def generate_answer(state:agentstate):
    """ you are a have to generate and answer from the existing
    state based on the message and from the retrieved docs and question
    """
    messages= state.messages
    question= state.messages[0].content
    ## this is the retrievd docs
    context= state.messages[-1].content
    
    # Prompt template
    prompt = ChatPromptTemplate.from_template(
    """Answer the question based on this context:
    
    Context: {context}
    
    Question: {question}
    
    Answer:"""
)
    
    llm= model
    
    formatted_messages = prompt.format_messages(context=context, question=question)
    result = llm.invoke(formatted_messages)
    
    return {"messages": [AIMessage(content=result.content)]}

## the rewriter 
from langchain_core.messages import HumanMessage
def rewriter(state:agentstate):
    """
    Transform the query to produce a better question.

    Args:
        state (messages): The current state

    Returns:
        dict: The updated state with re-phrased question
    """

    print("---TRANSFORM QUERY---")
    messages = state.messages
    question = messages[0].content

    msg = [
        HumanMessage(
            content=f""" \n 
    Look at the input and try to reason about the underlying semantic intent / meaning. \n 
    Here is the initial question:
    \n ------- \n
    {question} 
    \n ------- \n
    Formulate an improved question: """,
        )
    ]

    # Grader
    llm = model
    response = model.invoke(msg)
    return {"messages": [response]}



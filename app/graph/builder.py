from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt.tool_node import ToolNode, tools_condition
from app.core.state import agentstate
from app.graph.edges import grade_documents
from app.graph.nodes import agent, generate_answer, rewriter
from app.tools.arxiv_tool import arxiv
from app.tools.tavily_tool import tavily
from app.tools.retriever_tools import technicalretrievar, healthretriever_tool
tools=[technicalretrievar, healthretriever_tool, arxiv, tavily]
builder= StateGraph(agentstate)
builder.add_node("agent", agent)
builder.add_node("rewriter", rewriter)
builder.add_node("generator", generate_answer)
TooLs =ToolNode(tools)
builder.add_node("tools",TooLs)

builder.add_edge(START, "agent")
builder.add_conditional_edges(
    "agent",
    tools_condition,
    {
        "tools":"tools",
        END:END,
    },

)

builder.add_conditional_edges(
    "tools",
    grade_documents,
)
builder.add_edge("generator", END)

builder.add_edge("rewriter", "agent")
graph = builder.compile()
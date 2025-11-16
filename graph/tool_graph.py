from state import State
from llm.tool_llm import llm_with_tools, tools
from tools.tool_node import get_tool_node

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt.tool_node import tools_condition


def tool_calling_llm(state: State):
    """
    The LLM decides:
    - Should I answer directly?
    - Or should I call a tool?
    """
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


def build_tool_graph():
    graph = StateGraph(State)

    # Nodes
    graph.add_node("llm", tool_calling_llm)
    graph.add_node("tools", get_tool_node(tools))

    # Start → LLM
    graph.add_edge(START, "llm")

    # LLM → either END or Tools
    graph.add_conditional_edges(
        "llm",
        tools_condition,
        {
            "__end__": END,      # LLM answers → END
            "tools": "tools"     # LLM triggers a tool → tools node
        }
    )

    # Tool → LLM (loop continues)
    graph.add_edge("tools", "llm")

    return graph.compile()

from langgraph.prebuilt import ToolNode

def get_tool_node(tools):
    """Return a ToolNode for LangGraph execution."""
    return ToolNode(tools)

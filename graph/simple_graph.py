from state import State
from llm.groq_client import llm
from langgraph.graph import StateGraph, START, END

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

def build_simple_graph():
    graph = StateGraph(State)
    graph.add_node("chat", chatbot)
    graph.add_edge(START, "chat")
    graph.add_edge("chat", END)
    return graph.compile()

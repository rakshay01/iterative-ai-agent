from llm.groq_client import llm
from tools.search_tool import search_tool
from tools.math_tool import multiply

# Tools list
tools = [search_tool, multiply]

# Bind tools to LLM
llm_with_tools = llm.bind_tools(tools)

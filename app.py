from graph.tool_graph import build_tool_graph
from langchain_core.messages import HumanMessage
import time

# Build the looping agent graph
graph = build_tool_graph()

if __name__ == "__main__":
    print("\n🤖 LangGraph LLM Tool Looping Agent")
    print("Type 'exit' to quit.\n")

    messages = []
    
    while True:
        try:
            user = input("You: ")
        except EOFError:
            print("\nBot: Goodbye!")
            break

        if user.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break

        # Keep only recent messages to avoid token limit
        if len(messages) > 10:
            messages = messages[-10:]
        
        messages.append(HumanMessage(content=user))
        
        try:
            print("Bot: Processing...")
            result = graph.invoke({"messages": messages})
            
            final_message = result["messages"][-1]
            print("Bot:", final_message.content)
            
            # Update messages for next iteration
            messages = result["messages"]
            
        except Exception as e:
            error_msg = str(e)
            if "rate_limit_exceeded" in error_msg or "Request too large" in error_msg:
                print("Bot: API rate limit reached. Please wait a moment before trying again.")
                print("     (Free tier limited to 6000 tokens/minute)")
                time.sleep(5)
                # Clear messages to reduce token usage
                messages = [HumanMessage(content=user)]
            else:
                print(f"Bot: Error - {error_msg[:100]}...")

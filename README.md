# Iterative AI Agent - LLM Tool Looping System

A practical AI agent built with LangGraph that combines language models with real tools to solve problems intelligently. The agent automatically decides whether to answer questions directly or use available tools like web search and math calculations. It then loops back to refine answers based on tool results.

## What This Project Does

This is an interactive chatbot agent that can:

- **Answer questions directly** when it has enough information
- **Search the web** using Tavily Search to get current information (news, weather, facts)
- **Perform math calculations** with custom calculation tools
- **Loop intelligently** - it uses tools when needed and then processes the results to give you better answers

The magic happens in the looping system: instead of just calling a tool once, the LLM evaluates tool results and can decide to use more tools or provide a final answer.

## Project Structure

Here's how the files are organized:

```
iterative-ai-agent/
├── app.py                 # Main entry point - runs the chatbot
├── config.py              # Configuration and environment variable loading
├── state.py               # Defines the conversation state structure
├── requirements.txt       # All Python packages needed
├── .env                   # Your API keys (create this)
│
├── llm/                   # Large Language Model setup
│   ├── groq_client.py    # Connects to Groq API (LLaMA 3.1 model)
│   └── tool_llm.py       # Binds tools to the LLM
│
├── tools/                 # Available tools for the agent
│   ├── math_tool.py      # Basic math operations (multiply, etc)
│   ├── search_tool.py    # Web search via Tavily
│   └── tool_node.py      # Manages tool execution
│
└── graph/                 # The AI agent workflow
    ├── tool_graph.py     # Main agent loop definition
    └── simple_graph.py   # Alternative simpler version
```

## Prerequisites - What You Need Before Starting

Before you can run this project, make sure you have:

### 1. Python Installed
You need Python 3.8 or higher. Check if you have it:
```bash
python --version
```

If you don't have Python, download it from [python.org](https://www.python.org/downloads/) and install it.

### 2. pip (Python Package Manager)
This usually comes with Python. Check:
```bash
pip --version
```

### 3. API Keys
You'll need two free API keys:

**a) Groq API Key** (for the LLM - the brain of the agent)
- Go to [console.groq.com](https://console.groq.com)
- Sign up for a free account
- Create an API key
- You get free usage with rate limits (6000 tokens per minute on free tier)

**b) Tavily API Key** (for web search)
- Go to [tavily.com](https://tavily.com)
- Sign up for a free account
- Get your API key
- Free tier includes web search capability

## Installation - Step by Step

### Step 1: Clone or Download This Project
```bash
cd "your-folder-path/iterative-ai-agent"
```

### Step 2: Create a Virtual Environment
A virtual environment keeps this project's dependencies separate from your system Python.

**On Windows (PowerShell or Command Prompt):**
```bash
python -m venv venv
```

**On Mac/Linux:**
```bash
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment
This ensures you're using the isolated Python environment for this project.

**On Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**On Mac/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line, indicating the environment is active.

### Step 4: Install Required Packages
Install all the Python packages this project needs:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and installs:
- **langgraph** - The framework for building agent workflows
- **langchain** - Building blocks for LLM applications
- **langsmith** - Monitoring and debugging LLM calls
- **langchain-groq** - Connection to Groq's LLaMA model
- **langchain_tavily** - Integration with Tavily web search
- **python-dotenv** - Loads environment variables from .env file

The installation might take a couple of minutes.

### Step 5: Create the .env File
Create a file named `.env` in the main project folder with your API keys:

```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

**Important:**
- Replace the text with your actual API keys
- Keep this file private - never share it
- The .env file is already in .gitignore so it won't be committed to git

Example of what it should look like:
```
GROQ_API_KEY=gsk_Aa1B2c3D4e5F6g7H8i9J0k1L2m3N4o5P6
TAVILY_API_KEY=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
```

## Running the Project

### Start the Agent
Make sure your virtual environment is active (you should see `(venv)` in your terminal):

```bash
python app.py
```

You should see:
```
🤖 LangGraph LLM Tool Looping Agent
Type 'exit' to quit.

You:
```

Now you can start chatting!

### Example Conversations

**Example 1 - Web Search:**
```
You: What's the weather in New York today?
Bot: Processing...
Bot: The weather in New York is... [searches web and provides current info]
```

**Example 2 - Math Calculation:**
```
You: What is 6 multiply 7?
Bot: Processing...
Bot: The result of 6 multiplied by 7 is 42.
```

**Example 3 - Complex Query:**
```
You: Who won the latest award and what year was it?
Bot: Processing...
Bot: [Searches web, finds information, and answers based on current data]
```

### Exit the Program
Simply type:
```
exit
```
or
```
quit
```

## How the Agent Works (Behind the Scenes)

The agent follows this flow:

1. **You ask a question** → Your message goes to the LLM
2. **LLM thinks** → It decides if it can answer or needs a tool
3. **Decision point:**
   - If it can answer directly → Returns your answer (END)
   - If it needs more info → Calls a tool (web search, math, etc)
4. **Tool executes** → Search tool queries the web, math tool calculates
5. **Loop back** → LLM gets tool results and can:
   - Answer your question with new information
   - Call another tool if needed
   - Or ask for clarification
6. **Final answer** → Agent returns the best response it could find

This looping is the power of the system - it's not just one call, but a complete workflow.

## Common Issues & Solutions

### "API Key not found" Error
**Problem:** The .env file isn't being read
**Solution:** 
- Make sure your .env file is in the main project folder (same level as app.py)
- Make sure it has exactly this format:
```
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```

### "Request too large" Error (Rate Limit)
**Problem:** Groq free tier limits tokens per minute
**Solution:**
- This is normal on free tier with 6000 tokens/minute limit
- The app will automatically wait and retry
- Upgrade to Groq Dev Tier or use shorter queries
- The app keeps only the last 10 messages to save tokens

### "Module not found" Error
**Problem:** Python packages not installed
**Solution:**
- Make sure virtual environment is active (`(venv)` in terminal)
- Run: `pip install -r requirements.txt` again

### Virtual Environment Not Active
**Problem:** You see errors about missing modules
**Solution:**
- Check if `(venv)` appears at the start of your terminal line
- If not, activate it:
  - Windows: `.\venv\Scripts\Activate.ps1`
  - Mac/Linux: `source venv/bin/activate`

## Project Details

### Technologies Used
- **LangGraph** - Graph-based orchestration of LLM workflows
- **LangChain** - Building blocks for connecting LLMs with tools
- **Groq API** - Fast LLaMA 3.1 language model
- **Tavily** - Real-time web search API
- **Python 3.8+** - Programming language

### Key Features
- ✅ Interactive conversational interface
- ✅ Automatic tool selection by the LLM
- ✅ Looping mechanism - LLM can use multiple tools
- ✅ Real-time web search capability
- ✅ Built-in error handling and rate limit management
- ✅ Clean separation of concerns (tools, LLM, graph)
- ✅ Environment variable configuration

### File Descriptions

**app.py** - The main application
- Handles user input and output
- Manages the chat loop
- Includes error handling for API rate limits

**state.py** - Defines conversation structure
- Uses TypedDict for type safety
- Manages message history

**config.py** - Loads API keys
- Reads from .env file
- Makes keys available to the application

**llm/groq_client.py** - LLM initialization
- Connects to Groq API with your key
- Uses LLaMA 3.1 8B model (free tier)

**llm/tool_llm.py** - Binds tools to LLM
- Tells the LLM what tools are available
- The LLM can then decide to use them

**tools/search_tool.py** - Web search capability
- Uses Tavily API
- Returns top 3 results

**tools/math_tool.py** - Math operations
- Simple custom tool example
- Shows how to create custom tools

**graph/tool_graph.py** - The agent workflow
- Defines the flow: LLM → Decision → Tools → Loop
- Orchestrates the entire interaction

## Customization - Make It Your Own

### Add More Tools
Want to add a new tool? Here's how:

1. Create a new file in `tools/` folder
2. Define your tool function
3. Add it to the tools list in `llm/tool_llm.py`

Example - Add a weather tool:
```python
# tools/weather_tool.py
def get_temperature(city: str) -> str:
    """Get current temperature for a city."""
    # Your code here
    return "Temperature: 72°F"
```

Then in `llm/tool_llm.py`:
```python
from tools.weather_tool import get_temperature
tools = [search_tool, multiply, get_temperature]  # Add your tool
```

### Change the LLM Model
In `llm/groq_client.py`, change the model:
```python
# Change from:
llm = ChatGroq(model="llama-3.1-8b-instant")

# To other available Groq models like:
llm = ChatGroq(model="mixtral-8x7b-32768")
```

### Adjust Token Limit
In `app.py`, change how many previous messages are kept:
```python
# Current: keeps last 10 messages
if len(messages) > 10:
    messages = messages[-10:]

# Change 10 to a different number based on your needs
```

## Tips for Best Results

1. **Be specific** - "Calculate 5 times 8" works better than "do some math"
2. **Ask recent info questions** - Weather, news, stock prices (search tools are good for these)
3. **Keep queries reasonable** - Shorter questions use fewer tokens
4. **Wait between searches** - Don't hit the API too fast if you have rate limits
5. **Check your API limits** - Visit Groq and Tavily consoles to see your usage

## Contributing & Improvements

This is a learning project. Some ideas for improvements:
- Add a database to store chat history
- Build a web interface instead of terminal
- Add more specialized tools (calculator, weather API, etc)
- Implement caching for common queries
- Add memory system for multi-turn conversations
- Create different agent types (research, customer support, etc)

## License & Credits

This project demonstrates LangGraph and LangChain concepts. It uses:
- Groq for fast LLM inference
- Tavily for web search
- LangChain ecosystem for integration

Feel free to use this as a learning reference or starting point for your own agents.

## Need Help?

1. Check the **Common Issues** section above
2. Look at the LangGraph docs: [langgraph.com](https://langgraph.com)
3. Check LangChain docs: [langchain.com](https://langchain.com)
4. Review code comments in the Python files

---

**Happy building with AI agents! 🚀**

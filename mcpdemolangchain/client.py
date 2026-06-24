from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio
import os

MATHSERVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mathserver.py")

async def main():
    client = MultiServerMCPClient(
        {
            "Math": {
                "command": "python",
                "args": [MATHSERVER_PATH],
                "transport": "stdio",
            },
            "Weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable-http",
            }
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
    agent = create_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (5 + 7) * 6?"}]}
    )

    print("Math Response:", math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the weather like in New York City?"}]}
    )
    print("Weather Response:", weather_response["messages"][-1].content)

asyncio.run(main())

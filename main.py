from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """schema for a source used by the agent"""

    url:str = Field(description="the url of the source")

class AgentResponse(BaseModel):
    """schema for the response of the agent"""

    answer:str = Field(description="the answer to the question")
    sources:List[Source] = Field(default_factory=list, description="the sources used to answer the question")


llm = ChatOpenAI(model="gpt-5", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Sunnyvale, California?")]})
    print(result)


if __name__ == "__main__":
    main()

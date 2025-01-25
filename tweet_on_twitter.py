import asyncio
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent, Browser, BrowserConfig

api_key = "sk-xxxx"

async def search_and_reply():
    browser = Browser(
        config=BrowserConfig(
            cdp_url="http://localhost:9222",
            headless=False
        )
    )
    
    agent = Agent(
        task="""
        1. Go to https://twitter.com/elonmusk
        2. Wait for the page to load completely
        3. Look for Elon Musk's most recent tweet
        4. Click the reply button on that tweet
        5. Type "awesome" in the reply field
        6. Click the Post/Reply button
        """,
        llm=ChatOpenAI(
            base_url='https://api.deepseek.com/v1',
            model='deepseek-chat',
            api_key=SecretStr(api_key),
        ),
        browser=browser,
        use_vision=False
    )
    
    await agent.run()

if __name__ == "__main__":
    asyncio.run(search_and_reply())

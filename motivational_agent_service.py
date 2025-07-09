from fastapi import FastAPI
from pydantic_ai import Agent
from pydantic_ai.providers.groq import GroqProvider
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

provider = GroqProvider(api_key=os.getenv("GROQ_API_KEY"))

motivational_agent = Agent(
    'groq:llama-3.3-70b-versatile',
    output_type=list[str],
    system_prompt="Give motivational quotes based on the user's fitness goals and current status.",
)

@app.get("/get_motivation")
async def get_motivation():
    result = await motivational_agent.run(
        "Please generate 5 motivational quotes about working out and eating healthy."
    )
    return result.data

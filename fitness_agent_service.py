from fastapi import FastAPI
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.providers.groq import GroqProvider
import os, httpx
from dotenv import load_dotenv

load_dotenv()

from models import FitnessProfile, FitnessReportResult 

app = FastAPI()

provider = GroqProvider(api_key=os.getenv("GROQ_API_KEY"))

fitness_agent = Agent(
    'groq:llama-3.3-70b-versatile',
    deps_type=FitnessProfile,
    output_type=FitnessReportResult,
    output_retries=3,
    system_prompt=(
        "Create a personalized FitnessReportResult based on user's information provided. "
        "For the meal_plan, each meal must have the following fields: name (str), ingredients (list of strings), portions (list of strings, one for each ingredient), and timing (breakfast, lunch, dinner, snack). "
        "For motivational quotes call the get_motivation tool and pick the single best one from the list you receive."
    )
)

@fitness_agent.system_prompt
async def add_user_fitness_data(ctx: RunContext[FitnessProfile]) -> str:
    return f"User fitness profile and goals: {ctx.deps!r}"

@fitness_agent.tool
async def get_motivation(ctx: RunContext) -> list[str]:
    async with httpx.AsyncClient() as client:
        response = await client.get(os.getenv("MOTIVATIONAL_AGENT_URL"))
        response.raise_for_status()
        return response.json()

async def analyze_profile(profile: FitnessProfile):
    result = await fitness_agent.run(
        "Create a personalized fitness and nutrition plan. The meal_plan must be a list of meals, each with name, ingredients, portions, and timing.",
        deps=profile
    )
    return result.data

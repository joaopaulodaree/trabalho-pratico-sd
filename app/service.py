from pydantic_ai import Agent, RunContext
from app.models import FitnessProfile, FitnessReportResult
from pydantic_ai.providers.groq import GroqProvider
from dotenv import load_dotenv
import os

load_dotenv()

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

motivational_agent = Agent(
    'groq:llama-3.3-70b-versatile',  
    output_type=list[str],
    system_prompt="Give motivational quotes based on the user's fitness goals and current status.",
)


@fitness_agent.system_prompt
async def add_user_fitness_data(ctx: RunContext[FitnessProfile]) -> str:
    fitness_data = ctx.deps
    return f"User fitness profile and goals: {fitness_data!r}"


@fitness_agent.tool
async def get_motivation(ctx: RunContext) -> list[str]:
    return await motivational_agent.run(
        f"Please generate 5 motivational quotes about working out and eating healthy.")
import os
from pydantic_ai import Agent, RunContext
from pydantic_ai.providers.groq import GroqProvider
from app.models import FitnessProfile, FitnessReportResult
from app.motivational_agent_service import get_motivational_quotes

provider = GroqProvider(api_key=os.getenv("GROQ_API_KEY"))

fitness_agent = Agent(
    "groq:llama3-70b-8192",
    deps_type=FitnessProfile,
    output_type=FitnessReportResult,
    output_retries=3,
    system_prompt="Create a personalized fitness and nutrition plan based on the user's profile. Use the motivation tool when appropriate."
)

@fitness_agent.tool
async def get_motivation(_: RunContext[FitnessProfile]) -> list[str]:
    return await get_motivational_quotes()

@fitness_agent.system_prompt
async def append_user_context(ctx: RunContext[FitnessProfile]) -> str:
    return f"User profile and goals: {ctx.deps}"

async def run_fitness_agent(profile: FitnessProfile) -> FitnessReportResult:
    return (await fitness_agent.run("Generate a complete fitness and meal plan for the user.", deps=profile)).output

async def analyze_profile(profile: FitnessProfile) -> FitnessReportResult:
    result = await fitness_agent.run(
        "Create a personalized fitness and nutrition plan. The meal_plan must be a list of meals, each with name, ingredients, portions, and timing.",
        deps=profile
    )
    return result.output


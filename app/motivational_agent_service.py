from pydantic_ai import Agent
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIModel

motivational_agent = Agent(
    'groq:llama-3.3-70b-versatile',  
    output_type=list[str],
    system_prompt="Give motivational quotes based on the user's fitness goals and current status.",
)

async def get_motivational_quotes() -> list[str]:
    return await motivational_agent.run("Please generate 5 motivational quotes about working out and eating healthy.")

from pydantic_ai import Agent, RunContext
from models import FitnessProfile, FitnessReportResult
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
    system_prompt="Crie um FitnessReportResult personalizado com base nas informações fornecidas pelo usuário. "
    "Para frases motivacionais, chame a ferramenta get_motivation e escolha a melhor frase da lista recebida."
)

motivational_agent = Agent(
    'groq:llama-3.3-70b-versatile',  
    output_type=list[str],
    system_prompt="Forneça frases motivacionais baseadas nos objetivos fitness e status atual do usuário.",
)

@fitness_agent.system_prompt
async def add_user_fitness_data(ctx: RunContext[FitnessProfile]) -> str:
    fitness_data = ctx.deps
    return f"Perfil e objetivos do usuário: {fitness_data!r}"


@fitness_agent.tool
async def get_motivation(ctx: RunContext) -> list[str]:
    return await motivational_agent.run(
        f"Por favor, gere 5 frases motivacionais sobre treinar e se alimentar de forma saudável.")
    
    
async def analyze_profile(profile: FitnessProfile) -> FitnessReportResult:
    result = await fitness_agent.run("Crie um plano personalizado de treino e nutrição.", deps=profile)
    return result.data
from pydantic_ai.agent import Agent, RunContext
from .models import PerfilFitness, ResultadoRelatorioFitness
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

# Agente principal para análise fitness
agente_fitness = Agent(
    'llama3.2',
    api_base="http://localhost:11434/v1",
    deps_type=PerfilFitness,
    output_type=ResultadoRelatorioFitness,
    output_retries=3,
    system_prompt="Crie um ResultadoRelatorioFitness personalizado baseado no PerfilFitness fornecido. O relatório deve incluir um plano de treino detalhado, plano alimentar, ingestão calórica diária, distribuição de macronutrientes e outras informações relevantes para ajudar o usuário a alcançar seus objetivos fitness."
    "Para frases motivacionais, chame a ferramenta obter_motivacao e escolha a melhor frase da lista que você receber"
)

# Agente para gerar frases motivacionais
agente_motivacional = Agent(
    'mistral',
    api_base="http://localhost:11434/v1",
    output_type=list[str],
    system_prompt="Você é um gerador de frases motivacionais. Sua tarefa é fornecer uma lista de frases motivacionais que podem inspirar e encorajar indivíduos em sua jornada fitness. Cada frase deve ser única e inspiradora, baseada nos objetivos fitness e status atual do usuário.",
)

@agente_fitness.system_prompt
async def adicionar_dados_fitness_usuario(ctx: RunContext[PerfilFitness]) -> str:
    dados_fitness = ctx.deps
    return f"Perfil e objetivos do usuário: {dados_fitness!r}"

@agente_fitness.tool
async def obter_motivacao(ctx: RunContext[PerfilFitness]) -> list[str]:
    return await agente_motivacional.run(
        f"Por favor, gere 5 frases motivacionais sobre treinar e comer de forma saudável.")

async def analisar_perfil(perfil_fitness: PerfilFitness):
    resultado = await agente_fitness.run("Crie um relatório fitness personalizado baseado no perfil fornecido.")
    return resultado.output
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class NivelAtividade(str, Enum):
    SEDENTARIO = "sedentario"
    LEVEMENTE_ATIVO = "levemente_ativo"
    MODERADAMENTE_ATIVO = "moderadamente_ativo"
    MUITO_ATIVO = "muito_ativo"
    EXTREMAMENTE_ATIVO = "extremamente_ativo"
    ATLETA = "atleta"

class ObjetivoFitness(str, Enum):
    PERDA_PESO = "perda_peso"
    GANHO_MASSA = "ganho_massa"
    MANUTENCAO = "manutencao"
    RESISTENCIA = "resistencia"
    FORCA = "forca"

class Exercicio(BaseModel):
    nome: str
    descricao: str
    duracao: int  # em minutos
    tempo_descanso: int = Field(default=0, description="Tempo de descanso em segundos entre séries ou exercícios")
    repeticoes: int  # para exercícios de força
    series: int  # para exercícios de força
    equipamento_necessario: Optional[List[str]] = None

class Refeicao(BaseModel):
    nome: str
    descricao: str
    ingredientes: List[str]
    calorias: int
    proteina: float  # em gramas
    carboidratos: float  # em gramas
    gorduras: float  # em gramas
    horario: str = Field(..., description="cafe_da_manha, almoco, jantar, lanche, etc.")

class PerfilFitness(BaseModel):
    idade: int
    peso: float  # em kg
    altura: float  # em cm
    genero: str
    nivel_atividade: NivelAtividade
    objetivo_fitness: ObjetivoFitness
    restricoes_alimentares: List[str] = []
    lesoes: List[str] = []
    horario_preferido_treino: str
    equipamentos_disponiveis: List[str] = []
    dias_treino_por_semana: int

class ResultadoRelatorioFitness(BaseModel):
    plano_treino: List[Exercicio] = Field(..., description="Plano de treino detalhado para a semana")
    plano_alimentar: List[Refeicao] = Field(..., description="Plano alimentar detalhado para a semana")
    calorias_diarias: int = Field(..., description="Ingestão calórica diária total baseada no perfil")
    macros: dict = Field(..., description="Distribuição de macronutrientes recomendada baseada no perfil")
    total_proteina: float
    total_carboidratos: float
    total_gorduras: float
    cronograma_semanal: List[str] = Field(..., description="Cronograma semanal de treinos e refeições")
    dicas_conselhos: List[str] = Field(..., description="Dicas e conselhos personalizados baseados no perfil")
    frases_motivacionais: List[str] = Field(..., description="Frases motivacionais")

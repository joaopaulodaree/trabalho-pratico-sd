from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class NivelAtividade(str, Enum):
    SEDENTARIO = "sedentario"
    LEVE = "leve"
    MODERADO = "moderado"
    MUITO_ATIVO = "muito_ativo"
    ATLETA = "atleta"

class ObjetivoFitness(str, Enum):
    PERDA_PESO = "perda_peso"
    GANHO_MUSCULO = "ganho_musculo"
    MANUTENCAO = "manutencao"
    RESISTENCIA = "resistencia"
    FORCA = "forca"

class FitnessProfile(BaseModel):
    idade: int
    peso: float
    altura: float
    genero: str
    nivel_atividade: NivelAtividade
    objetivo_fitness: ObjetivoFitness
    restricoes_alimentares: List[str] = []
    lesoes: List[str] = []
    horario_preferido_treino: str
    equipamentos_disponiveis: List[str] = []
    dias_treino_por_semana: int
    


class Exercicio(BaseModel):
    nome: str
    series: int
    repeticoes: int
    tempo_descanso: int = Field(..., description="Tempo de descanso em segundos")

class Refeicao(BaseModel):
    nome: str
    calorias: int
    proteina: float
    carboidratos: float
    gorduras: float
    horario: str = Field(..., description="cafe_da_manha, almoco, jantar, lanche")
    

class FitnessReportResult(BaseModel):
    plano_treino: List[Exercicio] = Field(description="Rotina de treino personalizada")
    plano_alimentar: List[Refeicao] = Field(description="Plano alimentar diário")
    calorias_diarias: int = Field(description="Ingestão calórica diária recomendada")
    macros: dict = Field(description="Divisão recomendada de macronutrientes (proteína, carboidrato, gordura)")
    dicas: List[str] = Field(description="Dicas personalizadas de treino e nutrição")
    cronograma_semanal: dict = Field(description="Cronograma semanal de treinos e refeições")
    frase_motivacional: str = Field(description="Frase motivacional")
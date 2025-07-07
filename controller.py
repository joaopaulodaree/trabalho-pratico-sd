from fastapi import APIRouter
from models import FitnessProfile
from service import analyze_profile


router = APIRouter()


@router.post("/analisar")
async def analisar_fitness(perfil_fitness: FitnessProfile):
    return await analyze_profile(perfil_fitness)
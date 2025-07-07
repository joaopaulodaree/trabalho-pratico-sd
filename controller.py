from fastapi import APIRouter
from .service import analyze_profile
from .models import FitnessProfile

# Roteador para endpoints de fitness
router = APIRouter()

@router.post("/analyze")
async def analyze_fitness(fitness_profile: FitnessProfile):
    return await analyze_profile(fitness_profile)


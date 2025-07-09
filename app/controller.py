from fastapi import APIRouter
from app.models import FitnessProfile
from app.fitness_agent_service import analyze_profile


router = APIRouter()


@router.post("/analyze")
async def analyze_fitness(fitness_profile: FitnessProfile):
    return await analyze_profile(fitness_profile)
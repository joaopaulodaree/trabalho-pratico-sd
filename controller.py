from fastapi import APIRouter
from models import FitnessProfile
from fitness_agent_service import analyze_profile


router = APIRouter()


@router.post("/analyze")
async def analyze_fitness(fitness_profile: FitnessProfile):
    return await analyze_profile(fitness_profile)
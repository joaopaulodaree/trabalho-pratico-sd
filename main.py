from fastapi import FastAPI
from .controller import router

# Aplicação FastAPI 
app = FastAPI(title="AI Fitness Trainer")
app.include_router(router)
from fastapi import FastAPI
from controller import router

app = FastAPI(title="AI Fitness Trainer")
app.include_router(router)


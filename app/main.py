from fastapi import FastAPI
from app.controller import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="AI Fitness Trainer")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

# Caminho correto para a pasta frontend
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # sobe para a raiz do projeto
frontend_path = os.path.join(BASE_DIR, "frontend")

# Serve arquivos estáticos
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Serve index.html na raiz
@app.get("/")
def read_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))
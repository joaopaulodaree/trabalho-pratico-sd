# ⚽ Assistente de Escalações e Táticas com IAs Distribuídas

Projeto Prático da disciplina de Sistemas Distribuídos, do Professor André Salgado na Universidade Federal de Lavras.

## 🎯 Objetivo do Projeto

Desenvolver um sistema distribuído com múltiplos agentes de IA que se comunicam entre si, gerando:

- 📊 Análises táticas e técnicas personalizadas
- 🧠 Interpretação de dados de times reais
- 📝 Geração automática de planos táticos em formato JSON
- 🗣️ Narrações ou comentários técnicos baseados nas formações e dados do jogo

---

## 🧩 Visão Geral da Arquitetura

- 🧠 **Agente 1 (Groq API)**: coleta ou simula dados táticos e informações dos jogadores
- 🧠 **Agente 2 (Modelo Local)**: interpreta os dados e gera análises táticas ou comentários técnicos
- 🔗 **Comunicação entre agentes** via API HTTP (microserviços)
- 🐳 **Modelo local containerizado com Docker**

---

## 📦 Tecnologias Utilizadas

- Python 3.11+
- OpenAI-compatible APIs (via Groq)
- LLaMA3 (modelo local)
- FastAPI (API de orquestração)
- Docker (containerização do modelo local)
- GitHub (controle de versão)

---
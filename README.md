# Fitness Advisor

Sistema de consultoria fitness com inteligência artificial.

## O que faz

- Analisa seu perfil fitness
- Cria planos de treino personalizados
- Gera planos alimentares balanceados
- Calcula necessidades calóricas
- Oferece frases motivacionais

## Instalação

1. Clone o repositório
2. Instale o Ollama: https://ollama.com/download
3. Baixe os modelos:
   ```bash
   ollama pull llama3.2
   ollama pull mistral
   ```
4. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Execute o servidor:
```bash
uvicorn main:app --reload
```

Acesse: http://localhost:8000/docs

## Exemplo

Envie um POST para `/analisar` com seus dados:

```json
{
  "idade": 28,
  "peso": 70.5,
  "altura": 175,
  "genero": "masculino",
  "nivel_atividade": "moderadamente_ativo",
  "objetivo_fitness": "ganho_massa",
  "dias_treino_por_semana": 4
}
```

Receba planos personalizados de treino e alimentação.

## Tecnologias

- FastAPI
- Pydantic AI
- Ollama
- Python 3.8+

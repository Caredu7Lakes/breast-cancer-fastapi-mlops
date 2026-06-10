# Breast Cancer Prediction API

[![FastAPI ML API CI](https://github.com/Caredu7Lakes/breast-cancer-fastapi-mlops/actions/workflows/ci.yml/badge.svg)](https://github.com/Caredu7Lakes/breast-cancer-fastapi-mlops/actions/workflows/ci.yml)

API desenvolvida com FastAPI para disponibilizar um modelo de Machine Learning treinado para classificação de tumores mamários.

## Objetivo

Transformar um modelo treinado em notebook Jupyter em um serviço acessível via HTTP.

## Modelo utilizado

O modelo utilizado foi um Random Forest Classifier treinado com o dataset Breast Cancer Wisconsin, disponível no Scikit-Learn.

## Tecnologias

- Python
- Scikit-Learn
- FastAPI
- Uvicorn
- Pydantic
- Joblib

## Como executar

```bash
pip install -r requirements.txt
uvicorn app:app --reload

```

## Acesso ao Swagger

http://127.0.0.1:8000/docs

## Endpoint

POST /predict

## Como executar com Docker

Construa a imagem:

```bash
docker build -t breast-cancer-api .
```

Execute o container:

```bash
docker run -p 8000:8000 breast-cancer-api
```

Acesse a documentação Swagger:

```text
http://127.0.0.1:8000/docs
```

## Validação via Docker

A API foi executada com sucesso dentro de um container Docker.

Fluxo validado:

```text
Docker container
↓
FastAPI
↓
modelo_cancer.pkl
↓
Random Forest
↓
Resposta JSON com predição e probabilidades
```

Exemplo de resposta:

```json
{
  "predicao": 1,
  "classe": "Benigno",
  "probabilidade_classe_0": 0.14,
  "probabilidade_classe_1": 0.86
}
```


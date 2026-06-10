# Breast Cancer Prediction API

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
from pydantic import BaseModel
from fastapi import FastAPI
import joblib

app = FastAPI()

modelo = joblib.load("modelo_cancer.pkl")

class Paciente(BaseModel):
    mean_radius: float
    mean_texture: float
    mean_perimeter: float
    mean_area: float
    mean_smoothness: float
    mean_compactness: float
    mean_concavity: float
    mean_concave_points: float
    mean_symmetry: float
    mean_fractal_dimension: float
    radius_error: float
    texture_error: float
    perimeter_error: float
    area_error: float
    smoothness_error: float
    compactness_error: float
    concavity_error: float
    concave_points_error: float
    symmetry_error: float
    fractal_dimension_error: float
    worst_radius: float
    worst_texture: float
    worst_perimeter: float
    worst_area: float
    worst_smoothness: float
    worst_compactness: float
    worst_concavity: float
    worst_concave_points: float
    worst_symmetry: float
    worst_fractal_dimension: float

@app.post("/predict")
def predict(paciente: Paciente):

    dados = [[
        paciente.mean_radius,
        paciente.mean_texture,
        paciente.mean_perimeter,
        paciente.mean_area,
        paciente.mean_smoothness,
        paciente.mean_compactness,
        paciente.mean_concavity,
        paciente.mean_concave_points,
        paciente.mean_symmetry,
        paciente.mean_fractal_dimension,
        paciente.radius_error,
        paciente.texture_error,
        paciente.perimeter_error,
        paciente.area_error,
        paciente.smoothness_error,
        paciente.compactness_error,
        paciente.concavity_error,
        paciente.concave_points_error,
        paciente.symmetry_error,
        paciente.fractal_dimension_error,
        paciente.worst_radius,
        paciente.worst_texture,
        paciente.worst_perimeter,
        paciente.worst_area,
        paciente.worst_smoothness,
        paciente.worst_compactness,
        paciente.worst_concavity,
        paciente.worst_concave_points,
        paciente.worst_symmetry,
        paciente.worst_fractal_dimension
    ]]

    predicao = modelo.predict(dados)
    probabilidade = modelo.predict_proba(dados)

    return {
        "predicao": int(predicao[0]),
        "classe": "Benigno" if int(predicao[0]) == 1 else "Maligno",
        "probabilidade_classe_0": float(probabilidade[0][0]),
        "probabilidade_classe_1": float(probabilidade[0][1])
    }
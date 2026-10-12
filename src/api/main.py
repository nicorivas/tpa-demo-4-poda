from fastapi import FastAPI

from src.models.cartera import Ejecutivo
from src.services.asignador import asignar

app = FastAPI(title="Asignador de carteras")
EJECUTIVOS = [Ejecutivo("E01", "Lucía Ferrer", "Norte")]


@app.post("/asignaciones")
def crear_asignacion(cliente_id: str, zona: str) -> dict:
    return {"cliente_id": cliente_id, "ejecutivo_id": asignar(cliente_id, zona, EJECUTIVOS)}

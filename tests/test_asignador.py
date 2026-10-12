from src.models.cartera import Ejecutivo
from src.services.asignador import asignar


def test_asigna_al_ejecutivo_de_la_zona():
    ejecutivos = [Ejecutivo("E01", "Lucía Ferrer", "Norte")]
    assert asignar("N01", "Norte", ejecutivos) == "E01"


def test_sin_cupo_devuelve_none():
    lleno = Ejecutivo("E01", "Lucía Ferrer", "Norte", clientes=[f"C{i}" for i in range(18)])
    assert asignar("N01", "Norte", [lleno]) is None

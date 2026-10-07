from src.models.cartera import Ejecutivo

TOPE_CLIENTES = 18


def asignar(cliente_id: str, zona: str, ejecutivos: list[Ejecutivo]) -> str | None:
    """Devuelve el id del ejecutivo de la zona con cupo, o None si no hay."""
    for ejecutivo in ejecutivos:
        if ejecutivo.zona == zona and len(ejecutivo.clientes) < TOPE_CLIENTES:
            ejecutivo.clientes.append(cliente_id)
            return ejecutivo.id
    return None

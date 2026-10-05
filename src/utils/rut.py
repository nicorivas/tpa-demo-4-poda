def normalizar_rut(rut: str) -> str:
    """Deja el RUT sin puntos y con guion, por ejemplo 11111111-1."""
    limpio = rut.replace(".", "").replace("-", "").strip().upper()
    return f"{limpio[:-1]}-{limpio[-1]}"

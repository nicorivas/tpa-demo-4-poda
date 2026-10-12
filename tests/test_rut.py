from src.utils.rut import normalizar_rut


def test_normaliza_rut():
    assert normalizar_rut("11.111.111-1") == "11111111-1"

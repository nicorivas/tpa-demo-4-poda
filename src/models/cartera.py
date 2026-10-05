from dataclasses import dataclass, field


@dataclass
class Ejecutivo:
    id: str
    nombre: str
    zona: str
    clientes: list[str] = field(default_factory=list)

# Asignador de carteras de Arroyo

Responde siempre en español.

## Lo que el código no dice
- El dueño del proceso es Marcela Soto, jefa comercial. Ningún cambio de reglas se aprueba sin ella, ni subir el tope de 18 clientes por ejecutivo.
- Todo cambio en `reglas.md` lo revisa Andrés Pino antes de unirse a `main`.
- Prohibido subir o pegar RUT, correos o montos reales de clientes. Solo datos ficticios, con correos `ejemplo.invalid`.
- Un cliente con contrato vigente nunca se reasigna a mitad de trimestre.

## Comandos
- Pruebas: `pytest`
- Formato y estilo: `ruff format .` y `ruff check .`
- API: `uvicorn src.api.main:app --reload`

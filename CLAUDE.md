# Asignador de carteras de Arroyo

Este proyecto asigna carteras comerciales a ejecutivos de ventas.
Arroyo es una empresa ficticia de ejemplo.

## Estructura de carpetas
- `src/` contiene el código fuente.
- `src/api/` contiene los endpoints de la API.
- `src/models/` contiene los modelos de datos.
- `src/utils/` contiene utilidades.
- `tests/` contiene las pruebas con pytest.
- `data/` contiene los archivos CSV de ejemplo.
- `docs/` contiene la documentación.
- `scripts/` contiene scripts auxiliares.
- `reglas.md` contiene las reglas de asignación.

## Stack
- Python 3.11
- Flask para la API
- pandas para el procesamiento de datos
- pytest para pruebas
- black para formato, con líneas de 100 caracteres
- Las dependencias están en `requirements.txt`

## Comandos
- Instalar dependencias: `pip install -r requirements.txt`
- Correr pruebas: `pytest`
- Correr las pruebas de un archivo: `pytest tests/test_asignador.py`
- Formatear: `black .`
- Revisar el estilo: `flake8`
- Levantar la API: `flask run`
- Crear el entorno virtual: `python -m venv .venv`
- Activar el entorno: `source .venv/bin/activate`

## Convenciones de código
- Usar nombres de funciones en snake_case.
- Usar nombres de clases en PascalCase.
- Escribir docstrings en las funciones públicas.
- Mantener las funciones cortas.
- Evitar variables globales.
- Usar type hints cuando sea posible.
- Importar los módulos al inicio del archivo.
- Ordenar los imports alfabéticamente.
- No dejar código comentado.
- Escribir pruebas para cada función nueva.
- Usar f-strings en vez de format.
- Manejar las excepciones de forma explícita.
- Nombrar los tests con el prefijo test_.
- Los modelos van en src/models.
- Los endpoints van en src/api.
- Las utilidades van en src/utils.
- Evitar duplicar código.
- Usar nombres de variables claros.
- No usar abreviaturas poco claras.
- Revisar el código propio antes de pedir una revisión.

## Datos
- Está prohibido subir o pegar RUT, correos o montos reales de clientes. Solo datos ficticios en pruebas y ejemplos.
- Los archivos de ejemplo usan correos con el dominio ejemplo.invalid.

## Flujo de trabajo
- Usar mensajes de commit descriptivos.
- Hacer commits pequeños.
- Trabajar en ramas separadas.
- Abrir un pull request para cada cambio.
- Todo cambio en reglas.md lo revisa Andrés Pino antes de unirse a main.
- Responder siempre en español.

## Dominio
- Una cartera es el conjunto de clientes de un ejecutivo.
- La zona de un cliente puede ser Norte, Centro o Sur.
- Un cliente con contrato vigente nunca se reasigna a mitad de trimestre.
- El dueño del proceso de asignación es Marcela Soto, jefa comercial. Ningún cambio de reglas se aprueba sin ella.
- Subir el tope de 18 clientes por ejecutivo también necesita su aprobación.

## Notas generales
- Mantener este archivo actualizado.
- Consultar la carpeta docs para más detalle.
- Preguntar ante cualquier duda.
- Ante la duda, no inventar reglas: preguntar a quien corresponda.

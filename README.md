# Curso de Python

Curso práctico de Python desde cero. La parte **basic** sigue el temario de [midudev/curso-python](https://github.com/midudev/curso-python). La parte **intermediate** combina referencias de [W3Schools](https://www.w3schools.com/python/) y apoyo de IA.

## Estructura

| Bloque | Tema | Archivos |
|--------|------|----------|
| `01_basic` | Fundamentos (print, tipos, variables, input) | 6 |
| `02_flow_control` | Control de flujo (if/else, booleanos, listas) | 4 |
| `03_loops` | Bucles (while, for, range, funciones) | 4 |
| `04_logic` | Lógica y estructuras de datos (dicts, tuplas, challenges) | 6 |
| `05_regex` | Expresiones regulares | 2 |
| `06_request_ai_dates` | Fechas, HTTP requests y APIs de IA | 3 |
| `07_poo` | Programación orientada a objetos | 1 |
| `08_web_scraping` | Web scraping con BeautifulSoup | 3 |
| **Total basic** | | **29 archivos** |
| `intermediate/01_data_access` | Acceso a datos (JSON, CSV, SQLite, pandas) | 4 |
| `intermediate/02_async_await` | Programación asíncrona (asyncio, httpx) | 2 |
| `intermediate/03_api_rest` | API REST con FastAPI | 2 |
| `intermediate/04_machine_learning` | Machine Learning (pandas, scipy, numpy) | 2 |

## Requisitos

- Python 3.10+

### Con entorno virtual (recomendado)

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
```

### Sin entorno virtual

```bash
pip install -r requirements.txt
```

## Ejercicios

El repositorio incluye dos carpetas con ejercicios prácticos en la rama `ejercicios`:

| Carpeta | Descripción |
|---------|-------------|
| `ejercicios/` | Enunciados para practicar (con `# Tu código aquí:`) |
| `soluciones/` | Mismos ejercicios resueltos (para consultar) |

Los ejercicios cubren desde fundamentos básicos hasta machine learning, asincronía y APIs REST.



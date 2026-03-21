# 1. Imagen base
FROM python:3.12-slim

# 2. Configuración de variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV POETRY_VERSION=2.0.1
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /app

# 3. Dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Instalar Poetry
RUN pip install "poetry==$POETRY_VERSION"

# 5. Copiar solo el pyproject.toml (sin lock file)
COPY pyproject.toml ./

# 6. Resolver dependencias y exportar a requirements.txt, luego instalar con pip.
#    Esto evita completamente los problemas con poetry.lock desactualizado.
RUN poetry lock \
    && poetry export -f requirements.txt --output requirements.txt --without-hashes \
    && pip install -r requirements.txt

# 7. Copiar el resto del código
COPY . .

# 8. Comando de inicio
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
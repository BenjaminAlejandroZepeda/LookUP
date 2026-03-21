# 1. Imagen base
FROM python:3.12-slim

# 2. Configuración de variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
# Definimos la versión de poetry
ENV POETRY_VERSION=2.0.1
# Suprime el warning de pip al correr como root
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /app

# 3. Instalación de dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. INSTALAR POETRY PRIMERO (con pip)
RUN pip install "poetry==$POETRY_VERSION"

# 5. COPIAR ARCHIVOS DE CONFIGURACIÓN (Antes que el código)
COPY pyproject.toml poetry.lock* ./

# 6. CONFIGURAR E INSTALAR DEPENDENCIAS
# poetry lock --no-update regenera el lock file si el pyproject.toml cambió,
# sin actualizar las versiones ya resueltas.
RUN poetry config virtualenvs.create false \
    && poetry lock --no-update \
    && poetry install --no-interaction --no-ansi --no-root

# 7. COPIAR EL RESTO DEL CÓDIGO
COPY . .

# 8. COMANDO DE INICIO
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
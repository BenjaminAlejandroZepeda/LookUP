# 1. Imagen base ligera de Python
FROM python:3.12-slim

# 2. Configuración de variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

WORKDIR /app

# 3. Instalación de dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Instalar Poetry usando el lanzador de python
RUN poetry install --no-interaction --no-ansi --no-root

# 5. Copiar archivos de configuración de dependencias
COPY pyproject.toml poetry.lock* ./

# 6. Instalar dependencias (sin crear venv, usamos el global del contenedor)
RUN py -m poetry config virtualenvs.create false \
    && py -m poetry install --no-interaction --no-ansi --no-root

# 7. Copiar el resto del código
COPY . .

# 8. Comando para ejecutar la app (Render asigna el PORT automáticamente)
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT}"]
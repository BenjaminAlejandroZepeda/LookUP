# 1. Imagen base
FROM python:3.12-slim

# 2. Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /app

# 3. Dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Instalar dependencias directo con pip (sin Poetry)
#    Las versiones mínimas vienen del pyproject.toml
RUN pip install \
    "fastapi>=0.135.1,<0.136.0" \
    "uvicorn>=0.42.0,<0.43.0" \
    "matplotlib>=3.10.8,<4.0.0" \
    "python-dotenv>=1.2.2,<2.0.0" \
    "supabase>=2.28.2,<3.0.0" \
    "pandas>=3.0.0"

# 5. Copiar el código
COPY . .

# 6. Comando de inicio
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
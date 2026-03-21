# LookUP API 

**Stack:** FastAPI · Poetry 2.0 · Docker · Supabase · GitHub Actions · Render

Render: https://lookup-1-rixc.onrender.com/

FastApi: https://lookup-1-rixc.onrender.com/docs#/

## 1. Arquitectura del Proyecto
 
```
LookUP/
├── .github/workflows/  # Pipelines de CI/CD
├── src/                # Código fuente de la API
├── tests/              # Tests unitarios
├── Dockerfile          # Receta del contenedor
├── pyproject.toml      # Dependencias (Poetry)
└── README.md           # Esta documentación
```

## 2. Configuración del Entorno Local

### Requisitos previos

- Python 3.12+
- Poetry 2.0 

### Instalación

```powershell
# Clonar el repositorio
git clone https://github.com/BenjaminAlejandroZepeda/LookUP
cd LookUP

# Instalar dependencias (incluyendo dev)
py -m poetry install
```

### Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
SUPABASE_URL=tu_url_de_supabase
SUPABASE_KEY=tu_key_de_supabase
```

### Ejecutar en desarrollo

```powershell
py -m poetry run uvicorn src.main:app --reload
```


## 3. Base de Datos (Supabase)

Este proyecto utiliza **Supabase** como plataforma de Backend-as-a-Service (BaaS), actuando como una capa de conexión rápida hacia una base de datos **PostgreSQL**. 

En lugar de gestionar un servidor SQL complejo, la API interactúa con la base de datos de la siguiente manera:
* **Motor:** PostgreSQL (gestionado en la nube por Supabase).
* **Conexión:** Se realiza a través de HTTPS utilizando la librería `supabase-py` dentro del contenedor Docker.
* **Seguridad:** Las credenciales (`SUPABASE_URL` y `SUPABASE_KEY`) nunca se exponen en el código fuente; se inyectan dinámicamente en Render a través de variables de entorno.
* **Uso en el Proyecto:** Funciona como la capa de persistencia principal, ideal para almacenar registros, usuarios o historiales de procesamiento de datos de forma relacional.

---

## 4. Pipeline de CI/CD

El pipeline de integración y despliegue continuo está automatizado con GitHub Actions. El archivo `.github/workflows/main.yml` se activa automáticamente en cada `push` o `pull_request` a la rama `main`, garantizando que solo el código que pasa las pruebas llegue a producción:

```text
Push a main
    │
    ▼
┌─────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│  Job: test  │────▶│  Job: deploy     │────▶│  Render Build       │
│             │     │  (solo en main)  │     │  (Docker Runtime)   │
│ • Checkout  │     │                  │     │                     │
│ • Python    │     │ • curl POST al   │     │ • docker build      │
│ • Poetry    │     │   Deploy Hook    │     │ • docker push       │
│ • pytest    │     │   de Render      │     │ • container deploy  │
└─────────────┘     └──────────────────┘     └─────────────────────┘
```


## 5. Despliegue en Render

### Configuración requerida en el Dashboard de Render

| Campo | Valor |
|---|---|
| Environment | **Docker** |
| Dockerfile Path | `./Dockerfile` |
| Docker Command | `uvicorn src.main:app --host 0.0.0.0 --port $PORT` |

### Secrets requeridos en GitHub

| Secret | Descripción |
|---|---|
| `RENDER_DEPLOY_HOOK` | URL del Deploy Hook generada en Render → Settings |

---

## Autor

**Benjamin Alejandro Zepeda**  
Ingeniería en Informática · Especialización IA  
[ben.zepeda@duocuc.cl](mailto:ben.zepeda@duocuc.cl)  
Marzo 2026

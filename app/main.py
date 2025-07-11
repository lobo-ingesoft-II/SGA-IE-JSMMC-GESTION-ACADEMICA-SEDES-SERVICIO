import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI,  Request, Response
from fastapi.middleware.cors import CORSMiddleware

import time
from prometheus_client import Counter, Histogram, CollectorRegistry, generate_latest, CONTENT_TYPE_LATEST
from app.config import settings
from app.db import init_db, test_connection
from app.routers import sedes

# Logging básico
logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Antes de arrancar
    init_db()
    test_connection()
    yield
    # Aquí podrías hacer limpieza al apagar, si hace falta

app = FastAPI(
    title="Sedes API",
    lifespan=lifespan
)

# ── 2. Definición de métricas Prometheus ────────────────────────────────────────
REQUEST_COUNT_SEDES = Counter(
    "http_requests_total_sedes",
    "Total de peticiones HTTP al servicio de sedes",
    ["method", "endpoint"]
)
REQUEST_LATENCY_SEDES = Histogram(
    "http_request_duration_seconds_sedes",
    "Duración de las peticiones HTTP al servicio de sedes",
    ["method", "endpoint"],
    buckets=[0.05, 0.1, 0.2, 0.3, 1.0, 2.5, 5.0]
)
ERROR_COUNT_SEDES = Counter(
    "http_request_errors_total_sedes",
    "Total de errores HTTP (status >= 400) en servicio de sedes",
    ["method", "endpoint", "status_code"]
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sedes.router, prefix="/sedes", tags=["Sedes"])

# ── 3. Middleware para capturar métricas ────────────────────────────────────────
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)
        status = response.status_code
    except Exception:
        status = 500
        raise
    finally:
        latency = time.time() - start_time
        endpoint = request.url.path
        method = request.method

        REQUEST_COUNT_SEDES.labels(method=method, endpoint=endpoint).inc()
        REQUEST_LATENCY_SEDES.labels(method=method, endpoint=endpoint).observe(latency)
        if status >= 400:
            ERROR_COUNT_SEDES.labels(
                method=method,
                endpoint=endpoint,
                status_code=str(status)
            ).inc()

    return response

# ── 4. Endpoint /metrics para Prometheus ───────────────────────────────────────
@app.get("/metrics")
def custom_metrics():
    registry = CollectorRegistry()
    registry.register(REQUEST_COUNT_SEDES)
    registry.register(REQUEST_LATENCY_SEDES)
    registry.register(ERROR_COUNT_SEDES)
    data = generate_latest(registry)
    return Response(data, media_type=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )

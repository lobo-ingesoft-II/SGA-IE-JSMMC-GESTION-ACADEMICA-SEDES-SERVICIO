from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import sedes
from app.db import init_db, test_connection

app = FastAPI(title="Sedes API")

# Habilitar CORS
origins = [
    "http://localhost:5173",  # ⚠️ Ajusta esto al origen real de tu frontend si es diferente
    "http://localhost:3000",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Usa ["*"] solo temporalmente si es necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()
    test_connection()

# Registrar rutas
app.include_router(sedes.router, prefix="/sedes", tags=["Sedes"])

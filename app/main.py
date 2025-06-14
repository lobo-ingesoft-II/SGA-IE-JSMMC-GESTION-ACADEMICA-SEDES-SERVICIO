from fastapi import FastAPI
from app.routers import sedes
from app.db import init_db, test_connection

app = FastAPI(title="Sedes API")

@app.on_event("startup")
def startup_event():
    init_db()
    test_connection()

# Registrar rutas
app.include_router(sedes.router, prefix="/sedes", tags=["Sedes"])
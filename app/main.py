import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

#Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)


app.include_router(sedes.router, prefix="/sedes", tags=["Sedes"])

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(
#         "app.main:app",
#         host=settings.HOST,
#         port=settings.PORT,
#         reload=settings.DEBUG,
#     )

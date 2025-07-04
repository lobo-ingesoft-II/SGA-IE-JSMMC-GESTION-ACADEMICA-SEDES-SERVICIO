import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

# Configurar logger para esta capa
logger = logging.getLogger(__name__)

# Crear el engine una sola vez, con echo en DEBUG
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=settings.DEBUG
)

# SessionLocal y Base para los modelos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    """Crea las tablas definidas en los modelos si no existen."""
    Base.metadata.create_all(bind=engine)

def test_connection():
    """
    Verifica que la base de datos responda correctamente.
    Registra el resultado en el logger en lugar de imprimir.
    """
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            logger.info("Database connection OK: %s", result.scalar())
    except Exception as e:
        logger.error("Database connection failed: %s", e)

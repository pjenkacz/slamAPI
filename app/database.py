from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Silnik bazy danych
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=False  #T2rue żeby widzieć SQL queries w konsoli
)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class dla modeli
Base = declarative_base()

# Dependency do uzyskania session w endpointach
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
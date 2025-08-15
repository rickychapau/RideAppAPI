import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Optional: load .env if present (does nothing if package not installed)
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# Prefer explicit driver; fall back to a sensible local default
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://ricky:mypassword123@localhost:5432/rideappdb"
)

# Create engine with safe defaults
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# db.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# 1. Engine (connection pool)
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # prevents stale connections
    pool_size=5,
    max_overflow=10           # disable in production
)

# 2. Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# 3. Base classes (IMPORTANT for your multi-schema design)
PublicBase = declarative_base()
ShopBase = declarative_base()

# 4. Dependency (used later in FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
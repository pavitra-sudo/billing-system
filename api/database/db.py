# db.py

import os
from fastapi import Request
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)

# Session
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# Base classes
PublicBase = declarative_base()
ShopBase = declarative_base()


def get_db(request: Request):
    db: Session = SessionLocal()

    try:
        schema = getattr(request.state, "schema", None)

        print("👉 Schema inside get_db:", schema)

        if schema:
            db.execute(text("SET search_path TO :schema"), {"schema": schema})

        yield db

    finally:
        db.close()
# Etablit la connection à la BDD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Update this with your actual database settings
DATABASE_URL = "postgresql+psycoph://postgres:password@localhost:5432/consultation_db"
EMBEDDING_MODEL="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
EMBEDDING_DIM=384

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
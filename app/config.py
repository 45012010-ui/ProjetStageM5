import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

M2_API_URL = os.getenv("M2_API_URL", "http://127.0.0.1:8000")
M3_API_URL = os.getenv("M3_API_URL", "http://127.0.0.1:8001")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL est manquant dans le fichier .env")
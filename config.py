from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/userdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = 'sdksdfanodnOINAIUBpiubpiubLKbskubISUBIUBEJKNBWUBQIOUFBNSJANSNKJBNAKJBDLKJnksdjfnlaasdOBEIUBO'

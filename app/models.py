# Génère les tables de la BDD
from sqlalchemy import UUID, Column, Float, ForeignKey, String, Text
from .db import Base

class Categorie(Base):
    __tablename__="categories"

    id = Column(UUID,  primary_key=True, index=True)
    nom = Column(String)

class Contribution(Base):
    __tablename__ = "contributions"

    id = Column(UUID,  primary_key=True, index=True)
    source_id = Column(String)
    titre = Column(String)
    corps = Column(Text)
    categorie_id = Column("categorie_id", UUID, ForeignKey("categories.id"), nullable=False)
    distance = Column(Float)
    similarite = Column(Float)

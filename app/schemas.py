# Validation des tables en utilisant Pydantic
from pydantic import UUID4, BaseModel
#from sqlalchemy import UUID, text

class CategorieCreate(BaseModel):
    nom : str

class CategorieRead(BaseModel):
    id : UUID4
    nom : str
        

class ContributionCreate(BaseModel):
    source_id : str
    titre : str
    corps : str
    categorie_id : UUID4
    distance : float
    similarite : float

class ContributionRead(BaseModel):
    id : UUID4
    source_id : str
    titre : str
    corps : str
    categorie_id : UUID4
    distance : float
    similarite : float

from pydantic import BaseModel, Field
from typing import Optional


# Classe para criar filme
class CriaFilme(BaseModel):
   # ID é autoincremento, então não estará no schema
   titulo: str
   ano_lancamento: int
   genero: str
   diretor: str


# Classe para alterar dados de filme
class UpdateFilme(BaseModel):
   # ID é autoincremento, então não estará no schema
   titulo: Optional[str] = Field(None, description="Título")
   ano_lancamento: Optional[int] = Field(None, description="Ano Lançamento")
   genero: Optional[str] = Field(None, description="Gênero")
   diretor: Optional[str] = Field(None, description="Diretor")
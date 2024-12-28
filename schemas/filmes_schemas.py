from pydantic import BaseModel


# Classe para criar filme
class CriaFilme(BaseModel):
   # ID é autoincremento, então não estará no schema
   titulo: str
   ano_lancamento: int
   genero: str
   diretor: str

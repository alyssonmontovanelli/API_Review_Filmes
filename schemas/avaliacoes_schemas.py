from pydantic import BaseModel

# Classe para criar filme
class CriaAvaliacao(BaseModel):
   # ID é autoincremento, então não estará no schema
   nome_avaliador: str
   filme_id: int
   nota: int
   comentario: str
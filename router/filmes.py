from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from schemas.filmes_schemas import CriaFilme

from config.db import SessionLocal
from config.db import conn
from models.filmes_models import Filme
from sqlalchemy.exc import SQLAlchemyError

# Sinalizando rotas
router = APIRouter(prefix="/filmes")



# Rotas - Puxar dados
@router.get("/")
def root():
   return {"message":"FastAPI"}


# Função para para evitar local_kw
def get_session_local():
   yield SessionLocal()

# Post - Adicionar um filme 
@router.post("/")
def adicionarFilme(data_filme: CriaFilme, db: Session = Depends(get_session_local)):
   try:
        # Criando um objeto Filme a partir dos dados do schema
        novo_filme = Filme(**data_filme.model_dump())

        # Adicionando o filme à sessão do banco de dados
        db.add(novo_filme)
        db.commit()  # Commit para garantir a persistência dos dados
        db.refresh(novo_filme)  # Atualiza o objeto com o ID gerado pelo banco

        return {"message": "Filme adicionado com sucesso!", "filme_id": novo_filme.id}
   except SQLAlchemyError as e:
        db.rollback()  # Rollback em caso de erro
        raise HTTPException(status_code=500, detail=f"Erro ao adicionar filme {e}")



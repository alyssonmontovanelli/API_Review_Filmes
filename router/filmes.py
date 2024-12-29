from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from schemas.filmes_schemas import CriaFilme, UpdateFilme

from config.db import SessionLocal
from config.db import conn
from models.filmes_models import Filme
from sqlalchemy.exc import SQLAlchemyError

from utils.request_api import requests, requestFilmeAPI, criaDictFilmeAPI

# Sinalizando rotas
router = APIRouter(prefix="/filmes")


# Função para para evitar local_kw
def get_session_local():
   yield SessionLocal()


#  ------------------------
# Endpoint - GET - Requisitar todos os filmes
@router.get("/")
def buscaFilmes(db: Session = Depends(get_session_local)):
   try:
      filmes = db.query(Filme).all()
      return filmes
   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Erro ao buscar filmes: \n{e}")

#  ------------------------
# Endpoint - GET - Requisitar filme com base no ID
@router.get("/{filme_id}")
def buscaFilmes(filme_id: str, db: Session = Depends(get_session_local)):
   try:
      filme_unico = db.query(Filme).filter(Filme.id == filme_id).first()
      if not filme_unico:
         raise HTTPException(status_code=404, detail="Filme não encontrado")
      return filme_unico
   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Erro ao buscar filme: \n{e}")

#  ------------------------
#  Endpoint - POST - Adicionar um filme 
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

# ------------------------------
# Endpoint - POST - Adiciona vários com base na API
@router.post("/reqapi/{nome_filme}")
def adicionarFilme_API(nome_filme: str, db: Session = Depends(get_session_local)):
   try:
      novo_filme_API = requestFilmeAPI(nome_filme)
      novo_filme = Filme(**novo_filme_API)
      
      # Adicionando o filme à sessão do banco de dados
      db.add(novo_filme)
      db.commit()  # Commit para garantir a persistência dos dados
      db.refresh(novo_filme)  # Atualiza o objeto com o ID gerado pelo banco

      return {"message": "Filme adicionado com sucesso!", "filme_id": novo_filme.id}
   except SQLAlchemyError as e:
      db.rollback()  # Rollback em caso de erro
      raise HTTPException(status_code=500, detail=f"Erro ao adicionar filme {e}")


#  ------------------------
#  Endpoint - PATCH - Atualizar dados
@router.patch("/patch/{filme_id}")
async def alteraAtributo(filme_id: str,
                          filme_data: UpdateFilme,
                          db: Session = Depends(get_session_local)):
   try:
      filme = db.query(Filme).filter(Filme.id == filme_id).first()
      if not filme:
         raise HTTPException(status_code=404, detail="Filme não encontrado")
      
      # Atualiza apenas os campos fornecidos
      for key, value in filme_data.model_dump(exclude_unset=True).items():
         setattr(filme, key, value)

      db.commit()
      db.refresh(filme)
      return filme

   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Erro ao atualizar filme: {e}")

#  ------------------------
#  Endpoint - DELETE - Deleta Filme
@router.delete("/delete/{filme_id}")
async def excluiFilme(filme_id: str, db: Session = Depends(get_session_local)):
   try:
      filme_unico = db.query(Filme).filter(Filme.id == filme_id).first()
      if not filme_unico:
         raise HTTPException(status_code=404, detail="Filme não encontrado")
      
      db.delete(filme_unico)
      db.commit()
      return f"Filme com ID nº: {filme_id} foi excluído com sucesso!"
   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Erro ao buscar filme: \n{e}")


# ------------------------------
# Endpoint - DELETE - Deleta todos os filmes



from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.avaliacoes_schemas import CriaAvaliacao
from config.db import SessionLocal
from models.avaliacao_models import Avaliacao
from sqlalchemy.exc import SQLAlchemyError

# Sinalizando rotas
router = APIRouter(prefix="/avaliacoes")

# Função para para evitar local_kw
def get_session_local():
   yield SessionLocal()

## Endpoint - GET - Requisitar todos as avaliações
@router.get("/")
def buscaAvaliacoes_All(db: Session = Depends(get_session_local)):
   try:
      avaliacoes = db.query(Avaliacao).all()
      return avaliacoes

   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Erro ao buscar filmes: \n{e}")


## Enpoint - POST - Cadastrar novas avaliações
@router.post("/")
def adicionaAvaliacao(data_avaliacao: CriaAvaliacao, db: Session = Depends(get_session_local)):
   try:
        # Criando um objeto Avaliação a partir dos dados do schema
      if not (1 <= data_avaliacao.nota <= 10):
         raise HTTPException(status_code=400, detail="A nota deve ser um valor entre 1 e 10.")

      nova_avaliacao = Avaliacao(**data_avaliacao.model_dump())

      # Adicionando o Avaliação à sessão do banco de dados
      db.add(nova_avaliacao)
      db.commit() 
      db.refresh(nova_avaliacao)  # Atualiza o objeto com o ID gerado pelo banco

      return {"message": "Review adicionado com sucesso!", "ID": nova_avaliacao.id}
   except SQLAlchemyError as e:
      db.rollback()  # Rollback em caso de erro
      raise HTTPException(status_code=500, detail=f"Erro ao adicionar Avaliação {e}")


## Endpoint - DELETE - Deletar avaliações 
@router.delete("/delete/{avaliacao_id}")
async def excluiAvaliacao(avaliacao_id: str, db: Session = Depends(get_session_local)):
   try:
      avaliacao_unica = db.query(Avaliacao).filter(Avaliacao.id == avaliacao_id).first()
      if not avaliacao_unica:
         raise HTTPException(status_code=404, detail="Avaliacao não encontrada")
      
      db.delete(avaliacao_unica)
      db.commit()
      return f"Review com ID nº {avaliacao_id} foi excluído com sucesso!"
   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Erro ao buscar Avaliaçãp: \n{e}")
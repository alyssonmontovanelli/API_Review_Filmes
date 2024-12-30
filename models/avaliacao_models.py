from sqlalchemy import ForeignKey, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

class Avaliacao(Base):
    __tablename__ = "tb_avaliacao"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome_avaliador = Column(String(225), nullable=False)
    filme_id = Column(Integer, ForeignKey("tb_filmes.id", ondelete="CASCADE"), nullable=False)
    nota = Column(Integer, nullable=False)
    comentario = Column(String(500), nullable=False)

    # Relacionamento com Filme (uma avaliação está associada a um único filme)
    filme = relationship("Filme", back_populates="avaliacoes")

from models.filmes_models import Filme


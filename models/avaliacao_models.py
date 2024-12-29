from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from config.db import Base


# avaliacao = Table("tb_avaliacao", meta_data,
#                Column("id", Integer, primary_key=True, index=True, autoincrement=True),
#                Column("nome_avaliador", String(225),nullable = False),
#                Column("filme_id", Integer, ForeignKey("tb_filme.id", ondelete = "CASCADE"), nullable = False),
#                Column("nota", Integer, nullable = False),
#                Column("comentario", String(500), nullable = False),
#                Column("filme", relationship("Filme", 
#                         back_populates = "avaliacoes")),
#                )


# meta_data.create_all(engine)

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


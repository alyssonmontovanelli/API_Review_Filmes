from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

# filmes = Table("tb_filmes", meta_data,
#                Column("id", Integer, primary_key=True, index=True, autoincrement=True),
#                Column("titulo", String(225),nullable = False),
#                Column("ano_lancamento", Integer, nullable = False),
#                Column("genero", String(50), nullable = False),
#                Column("diretor", String(225), nullable = False),
#                Column("avaliacoes", relationship("Avaliacao", 
#                              back_populates = "filme")),
#                )

# meta_data.create_all(engine)


class Filme(Base):
    __tablename__ = "tb_filmes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(225), nullable=False)
    ano_lancamento = Column(Integer, nullable=False)
    genero = Column(String(50), nullable=False)
    diretor = Column(String(225), nullable=False)

    # Relacionamento com Avaliacao (um filme pode ter muitas avaliações)
    avaliacoes = relationship("Avaliacao", back_populates="filme", cascade="all, delete-orphan")

# 
from models.avaliacao_models import Avaliacao

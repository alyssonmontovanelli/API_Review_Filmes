from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Engine
engine = create_engine("mysql+pymysql://root:12345678@localhost:3306/reviewFilmes")

conn = engine.connect()

meta_data = MetaData()

Base = declarative_base(metadata=meta_data)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar todas as tabelas no banco de dados
def create_tables():
    Base.metadata.create_all(bind=engine)

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
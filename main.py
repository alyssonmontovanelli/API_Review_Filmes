from fastapi import FastAPI
from config.db import create_tables
from router import filmes, avaliacoes

app = FastAPI()

create_tables()

app.include_router(filmes.router)
app.include_router(avaliacoes.router)
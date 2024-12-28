from fastapi import FastAPI
from config.db import create_tables
from router import filmes

app = FastAPI()

create_tables()

app.include_router(filmes.router)
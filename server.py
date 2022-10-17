import string
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import help
from database import get_db, criar_bd
from src.infra.sqlalchemy.repositorio.pergunta import RepositorioPergunta
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional #criar listagem em python
from pydantic import BaseModel
from uuid import uuid4 #criar id aleatoria

criar_bd()

app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware
 

banco: List[help] = [] #lista

@app.get("/helps")
async def listar_helps(db: Session = Depends(get_db)):
    listas = RepositorioPergunta(db).listar()
    return listas

@app.get("/helps/{help_id}")
async def obter_help(help_id: str):
    for help in banco:
        if help.id == help_id:
            return help
    return {"erro": "pergunta não encontrada"}

@app.delete("/helps/{help_id}")
async def remover_help(help_id: str):
    posicao = -1
    # buscar a posicao de pergunta
    for index, help in enumerate(banco): #enumerate retorna posicao e objeto
        if help.id == help_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {"mensagem": "Pergunta removida com sucesso!"}
    else:return {"erro": "Pergunta não localizada"}



@app.post("/helps")
async def criar_help(help: help, db: Session = Depends(get_db)):
    pergunta_criada = RepositorioPergunta(db).criar(help)
    help.id = str(uuid4())
    banco.append(help)
    return None
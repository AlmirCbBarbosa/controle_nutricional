from fastapi import APIRouter, Depends
from datetime import date
from models import Pessoa
from dependencies import pegar_sessao

#criando o router
pessoa_router = APIRouter(prefix="/pessoa", tags=["pessoa"])

#criando endpoints
@pessoa_router.get("/")
async def pessoa_raiz():
    return {"mensagem": "Você está na raiz de pessoa."}

@pessoa_router.post("/criar_pessoa")
async def criar_pessoa(nome:str, email:str, senha:str, data_nascimento:date, peso_ideal:float, altura:float, session= Depends(pegar_sessao)):
    pessoa = session.query(Pessoa).filter(Pessoa.email==email).first()
    if pessoa:
        return {"mensagem": "já existe pessoa cadastrada com este email"}
    else:
        nova_pessoa = Pessoa(nome, email, senha, data_nascimento, peso_ideal, altura) # a entrada de data deve ser YYYY-MM-DD
        session.add(nova_pessoa)
        session.commit()
        return {"mensagem": "pessoa criada com sucesso!"}
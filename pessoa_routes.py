from fastapi import APIRouter, Depends
from datetime import date
from models import Pessoa
from dependencies import pegar_sessao
from main import bcrypt_context

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
        senha_criptografada = bcrypt_context.hash(senha) # criptografando a senha criada pelo usuario
        nova_pessoa = Pessoa(nome, email, senha_criptografada, data_nascimento, peso_ideal, altura) # a entrada de data deve ser YYYY-MM-DD
        session.add(nova_pessoa)
        session.commit()
        return {"mensagem": "pessoa criada com sucesso!"}
    
    # continuar aula 4 28:00
from fastapi import APIRouter, Depends, HTTPException
from datetime import date
from models import Pessoa
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import PessoaSchema
from sqlalchemy.orm import Session #tipos de dados Session

#criando o router
pessoa_router = APIRouter(prefix="/pessoa", tags=["pessoa"])

#criando endpoints
@pessoa_router.get("/")
async def pessoa_raiz():
    return {"mensagem": "Você está na raiz de pessoa."}

@pessoa_router.post("/criar_pessoa")
async def criar_pessoa(pessoa_schema: PessoaSchema, session: Session = Depends(pegar_sessao)):
    pessoa = session.query(Pessoa).filter(Pessoa.email==pessoa_schema.email).first()
    if pessoa:
        raise HTTPException(status_code=400, detail="E-mail do usuário já cadastrado.")
    else:
        senha_criptografada = bcrypt_context.hash(pessoa_schema.senha) # criptografando a senha criada pelo usuario
        nova_pessoa = Pessoa(pessoa_schema.nome, pessoa_schema.email, senha_criptografada, pessoa_schema.data_nascimento, pessoa_schema.peso_ideal, pessoa_schema.altura) # a entrada de data deve ser YYYY-MM-DD
        session.add(nova_pessoa)
        session.commit()
        return {"mensagem": f"pessoa criada com sucesso! {pessoa_schema.email}"}
    
    # continuar aula 4 28:00
from fastapi import APIRouter

#criando o router
pessoa_router = APIRouter(prefix="/pessoa", tags=["pessoa"])

#criando endpoints
@pessoa_router.get("/")
async def pessoa_raiz():
    return {"mensagem": "Você está na raiz de pessoa."}
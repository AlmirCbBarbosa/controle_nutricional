from fastapi import APIRouter

#criando o router
peso_router = APIRouter(prefix="/peso", tags=["peso"])

#criando endpoints
@peso_router.get("/")
async def peso_raiz():
    return {"mensagem": "Você está na raiz de peso."}
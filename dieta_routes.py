from fastapi import APIRouter

#criando o router
dieta_router = APIRouter(prefix="/dieta", tags=["dieta"])

#criando endpoints
@dieta_router.get("/")
async def pessoa_raiz():
    return {"mensagem": "Você está na raiz de dieta."}
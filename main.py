from fastapi import FastAPI
from passlib.context import CryptContext # modulo de criptografia
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


app = FastAPI() #para ativar o servidor, use o comando: uvicorn main:app --reload

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#adicionando as variaveis router
from pessoa_routes import pessoa_router
from peso_routes import peso_router
from dieta_routes import dieta_router

#adicionando os endpoints dos router
app.include_router(pessoa_router)
app.include_router(peso_router)
app.include_router(dieta_router)

#rota raiz do site
@app.get("/")
async def raiz():
    return {"mensagem": "Bem vindos à api Controle Nutricional!"}
from models import db
from sqlalchemy.orm import sessionmaker

#criar uma sessão do banco de dados
def pegar_sessao():
    try:    
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close() #encerra a sessão do banco de dados
        


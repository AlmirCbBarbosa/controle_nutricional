from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import declarative_base

#criação da conexão com o banco de dados
db = create_engine("sqlite:///banco.db")

#criando a base do banco de dados
Base = declarative_base()

#Criando as classes que darão origem aos bancos de dados

#pessoa
class Usuario(Base):
    __tablename__ = "pessoa"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    data_nascimento = Column("data_nascimento", Date)
    peso_ideal = Column("peso_ideal", Float, nullable=False)
    altura = Column("altura", Float, nullable=False)

    def __init__(self, nome, email, senha, data_nascimento, peso_ideal, altura):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_nascimento = data_nascimento
        self.peso_ideal = peso_ideal
        self.altura = altura

#peso
class Peso(Base):
    __tablename__ = "peso"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_pessoa = Column("id_pessoa", ForeignKey("pessoa.id"))
    peso = Column("peso", Float, nullable=False)
    data = Column("data", Date, nullable=False)

    def __init__(self, id_pessoa, peso, data):
        self.id_pessoa = id_pessoa
        self.peso = peso
        self.data = data

#dieta
class Dieta(Base):
    __tablename__ = "dieta"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_pessoa = Column("id_pessoa", ForeignKey("pessoa.id"))
    tipo = Column("tipo", String, nullable=False)
    calorias_dia = Column("calorias_dia", Float, nullable=False)
    carboidratos_dia = Column("carboidratos_dia", Float, nullable=False)
    proteinas_dia = Column("proteinas_dia", Float, nullable=False)
    gorduras_dia = Column("gorduras_dia", Float, nullable=False)
    data_inicio = Column("data_inicio", Date, nullable=False)
    data_termino = Column("data_termino", Date)

    def __init__(self, id_pessoa, tipo, calorias_dia, carboidratos_dia, proteinas_dia, gorduras_dia, data_inicio):
        self.id_pessoa = id_pessoa
        self.tipo = tipo
        self.calorias_dia = calorias_dia
        self.carboidratos_dia = carboidratos_dia
        self.proteinas_dia = proteinas_dia
        self.gorduras_dia = gorduras_dia
        self.data_inicio = data_inicio

    






from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

class PessoaSchema(BaseModel):
   nome: str = Field(..., min_length=2, max_length=100)
   email: EmailStr #validação de email do pydantic
   senha: str = Field(...,min_length=6, max_length=72) # 72 é o limite do bcrypt
   data_nascimento: date
   peso_ideal: float = Field(..., gt=0) # para aceitar valores positivos
   altura: float = Field(..., gt=0) # para aceitar valores positivos

   class Config:
      from_attributes = True



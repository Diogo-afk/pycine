from pydantic import BaseModel

"""
VALIDAÇÃO DO MODEL - CAMPOS NECESSÁRIOS PARA CRIAR UM USUÁRIO

"""

class MovieBase(BaseModel):
    """ Classe para fazer validacao """
    id: int
    tmdb_id: int
    title: str

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool    
    class Config:
        orm_mode = True
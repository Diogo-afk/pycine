from sqlalchemy import Boolean, Column, Integer, String
from database import Base

"""
CLASSE QUE É MAPEADA NA TABELA DO SQLITE (pycine.db)

"""

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


# Filmes favoritos

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    tmdb_id = Column(Integer)
    title = Column(String)
    # user_id


from operator import index
from sqlalchemy import Column, Integer, String
from database import Base

class help(Base):
    __tablename__ = 'perguntas'

    id = Column(Integer, primary_key=True, index=True)
    pergunta = Column(String)
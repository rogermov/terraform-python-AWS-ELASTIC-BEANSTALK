from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPergunta():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, pergunta: schemas.help):
        db_pergunta = models.help(pergunta=pergunta.pergunta) #contrutor de classe arrumar
                                                            

        self.db.add(db_pergunta)
        self.db.commit()
        self.db.refresh(db_pergunta) #revisar aqui
        return db_pergunta
                                  
    
    def listar(self):
        perguntas = self.db.query(models.help) .all()
        return perguntas

    def obter(self):
        pass

    def remover(self):
        pass
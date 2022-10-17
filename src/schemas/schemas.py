from pydantic import BaseModel
from typing import Optional, List


class help(BaseModel):
    id: Optional[str] = None
    pergunta: str

    class Config:
        orm_mode = True



from typing import Optional

from pydantic import BaseModel as SCBaseModel


class CursoSchema(SCBaseModel):
    id: Optional[int]
    tittulo: str
    aulas: int
    horas: int


    class Config:
        orm_mode = True

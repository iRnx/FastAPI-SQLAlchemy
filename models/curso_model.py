from core.configs import settings

from sqlalchemy import Column, Integer, String, BigInteger
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column


class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)



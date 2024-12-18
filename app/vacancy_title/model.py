from sqlalchemy import Column, Computed, Date, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.database import Base


class VacancyTitle(Base):
    __tablename__ = "vacancy_title"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)

    vacancy = relationship("Vacancy", back_populates="vacancy_title")

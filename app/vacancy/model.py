from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DATETIME, ForeignKey, Integer, Boolean, Text, String

from app.database import Base


class Vacancy(Base):
    __tablename__ = "vacancy"
    id = Column(Integer, primary_key=True, nullable=False)
    city_id = Column(Integer, ForeignKey('city.id', ondelete="CASCADE"), nullable=False)
    vacancy_title_id = Column(Integer, ForeignKey("vacancy_title.id", onupdate="CASCADE"), nullable=False)
    salary = Column(String(130), nullable=True)
    work_experience_id = Column(Integer, ForeignKey("work_experience.id", onupdate="CASCADE"), nullable=False)
    employment_rate_id = Column(Integer, ForeignKey("employment_rate.id", onupdate="CASCADE"), nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    description = Column(Text, nullable=True)
    created_at = Column(DATETIME, default=datetime.utcnow())
    updated_at = Column(DATETIME, default=datetime.utcnow())

    employment_rate = relationship("EmploymentRate", back_populates="vacancy")
    city = relationship("City", back_populates="vacancy")
    vacancy_title = relationship("VacancyTitle", back_populates="vacancy")
    work_experience = relationship("WorkExperience", back_populates="vacancy")

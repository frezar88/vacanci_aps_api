from datetime import datetime

from sqlalchemy import Column, Computed, DATETIME, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    token = Column(Text, nullable=True)
    created_at = Column(DATETIME, default=datetime.utcnow())

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class County(Base):
    __tablename__ = 'counties'

    county_id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)

    forecasts = relationship('CountyForecast', back_populates='county')
    users = relationship('User', back_populates='county')

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Forecast(Base):
    __tablename__ = 'forecasts'

    forecast_id = Column(Integer, primary_key=True)
    prediction = Column(String)
    recommended_activity = Column(String)
    weather = Column(String)
    temperature = Column(String)

    county_forecasts = relationship('CountyForecast', back_populates='forecast')

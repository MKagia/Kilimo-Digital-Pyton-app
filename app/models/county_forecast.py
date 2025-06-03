from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
import datetime

class CountyForecast(Base):
    __tablename__ = 'county_forecasts'

    id = Column(Integer, primary_key=True)
    forecast_id = Column(Integer, ForeignKey('forecasts.forecast_id'))
    county_id = Column(Integer, ForeignKey('counties.county_id'))
    date = Column(DateTime, default=datetime.datetime.utcnow)

    county = relationship('County', back_populates='forecasts')
    forecast = relationship('Forecast', back_populates='county_forecasts')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, nullable=False)
    county_id = Column(Integer, ForeignKey('counties.county_id'))

    county = relationship('County', back_populates='users')

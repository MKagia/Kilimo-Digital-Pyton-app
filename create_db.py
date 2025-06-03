from app.models import Base
from app.models import county, forecast, county_forecast, user
from sqlalchemy import create_engine

engine = create_engine("sqlite:///weather.db")

Base.metadata.create_all(engine)
print("Database created successfully.")

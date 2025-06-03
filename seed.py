from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app.models.county import County
from app.models.forecast import Forecast
from app.models.county_forecast import CountyForecast
from app.models.user import User
import datetime

DATABASE_URL = 'sqlite:///weather.db'

def seed_data():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Initial counties
    nairobi = County(location="Nairobi")
    kisumu = County(location="Kisumu")
    mombasa = County(location="Mombasa")
    eldoret = County(location="Eldoret")
    session.add_all([nairobi, kisumu, mombasa, eldoret])
    session.commit()

    # Forecasts
    forecast1 = Forecast(
        prediction="Sunny",
        recommended_activity="Irrigation and mulching to conserve moisture",
        weather="Clear",
        temperature="25C"
    )
    forecast2 = Forecast(
        prediction="Rainy",
        recommended_activity="Avoid planting in waterlogged areas, consider drainage",
        weather="Rain",
        temperature="18C"
    )
    forecast3 = Forecast(
        prediction="Cloudy",
        recommended_activity="Good time for soil testing and planning",
        weather="Clouds",
        temperature="22C"
    )
    forecast4 = Forecast(
        prediction="Stormy",
        recommended_activity="Secure farm structures and delay fertilizer application",
        weather="Storm",
        temperature="16C"
    )
    session.add_all([forecast1, forecast2, forecast3, forecast4])
    session.commit()

    # CountyForecast entries
    cf1 = CountyForecast(county_id=nairobi.county_id, forecast_id=forecast1.forecast_id, date=datetime.datetime.now())
    cf2 = CountyForecast(county_id=kisumu.county_id, forecast_id=forecast2.forecast_id, date=datetime.datetime.now())
    cf3 = CountyForecast(county_id=mombasa.county_id, forecast_id=forecast3.forecast_id, date=datetime.datetime.now())
    cf4 = CountyForecast(county_id=eldoret.county_id, forecast_id=forecast4.forecast_id, date=datetime.datetime.now())
    session.add_all([cf1, cf2, cf3, cf4])
    session.commit()

    # Users
    user1 = User(username="brian", email="briankagia@gmail.com", county_id=nairobi.county_id)
    user2 = User(username="lucy", email="lucychepkemoi@gmail.com", county_id=mombasa.county_id)
    user3 = User(username="mike", email="mikebaraza@gmail.com", county_id=eldoret.county_id)
    session.add_all([user1, user2, user3])
    session.commit()

    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_data()

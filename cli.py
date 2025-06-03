from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import County, Forecast, CountyForecast, User
from app.models.base import Base
from tabulate import tabulate

engine = create_engine("sqlite:///weather.db")
Session = sessionmaker(bind=engine)
session = Session()

def list_counties():
    counties = session.query(County).all()
    data = [(c.county_id, c.location) for c in counties]
    print(tabulate(data, headers=["ID", "Location"]))

def add_county():
    name = input("Enter county location: ")
    county = County(location=name)
    session.add(county)
    session.commit()
    print("County added.")

def list_forecasts():
    forecasts = session.query(Forecast).all()
    data = [(f.forecast_id, f.prediction, f.recommended_activity, f.weather, f.temperature) for f in forecasts]
    print(tabulate(data, headers=["ID", "Prediction", "Activity", "Weather", "Temp"]))

def add_forecast():
    pred = input("Prediction: ")
    activity = input("Recommended activity: ")
    weather = input("Weather: ")
    temp = input("Temperature: ")
    forecast = Forecast(prediction=pred, recommended_activity=activity, weather=weather, temperature=temp)
    session.add(forecast)
    session.commit()
    print("Forecast added.")

def main():
    print("\n=== Weather CLI ===")
    print("1. List counties")
    print("2. Add county")
    print("3. List forecasts")
    print("4. Add forecast")
    print("0. Exit")

    while True:
        choice = input("Choose an option: ")

        if choice == "1":
            list_counties()
        elif choice == "2":
            add_county()
        elif choice == "3":
            list_forecasts()
        elif choice == "4":
            add_forecast()
        elif choice == "0":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

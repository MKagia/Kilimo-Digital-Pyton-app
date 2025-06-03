from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app.models.county import County
from app.models.forecast import Forecast
from app.models.county_forecast import CountyForecast
from app.models.user import User
from tabulate import tabulate

# -------------------- Database Setup --------------------
engine = create_engine("sqlite:///weather.db")
Session = sessionmaker(bind=engine)
session = Session()

# -------------------- County --------------------
def list_counties():
    counties = session.query(County).all()
    if counties:
        data = [(c.county_id, c.location) for c in counties]
        print(tabulate(data, headers=["ID", "Location"]))
    else:
        print("No counties found.")

def add_county():
    name = input("Enter county location: ")
    if name:
        county = County(location=name)
        session.add(county)
        session.commit()
        print("County added.")
    else:
        print("Invalid county name.")

# -------------------- Forecast --------------------
def list_forecasts():
    forecasts = session.query(Forecast).all()
    if forecasts:
        data = [(f.forecast_id, f.prediction, f.recommended_activity, f.weather, f.temperature) for f in forecasts]
        print(tabulate(data, headers=["ID", "Prediction", "Activity", "Weather", "Temp"]))
    else:
        print("No forecasts found.")

def add_forecast():
    pred = input("Prediction: ")
    activity = input("Recommended activity: ")
    weather = input("Weather: ")
    temp = input("Temperature: ")

    forecast = Forecast(
        prediction=pred,
        recommended_activity=activity,
        weather=weather,
        temperature=temp
    )
    session.add(forecast)
    session.commit()
    print("Forecast added.")

# -------------------- County Forecast View --------------------
def list_counties_with_forecasts():
    counties = session.query(County).all()
    for county in counties:
        print(f"\nCounty: {county.location}")
        if county.forecasts:
            for cf in county.forecasts:
                forecast = cf.forecast
                print(f"  - Date: {cf.date.strftime('%Y-%m-%d')}")
                print(f"    Prediction: {forecast.prediction}")
                print(f"    Weather: {forecast.weather}, Temp: {forecast.temperature}")
                print(f"    Activity: {forecast.recommended_activity}")
        else:
            print("  No forecasts found.")

# -------------------- Users --------------------
def list_users():
    users = session.query(User).all()
    if users:
        data = [
            (u.user_id, u.username, u.email, u.county.location if u.county else "N/A")
            for u in users
        ]
        print(tabulate(data, headers=["ID", "Username", "Email", "County"]))
    else:
        print("No users found.")

# -------------------- Main Menu --------------------
def main():
    while True:
        print("\n=== Weather CLI ===")
        print("1. List counties")
        print("2. Add county")
        print("3. List forecasts")
        print("4. Add forecast")
        print("5. List counties with forecasts")
        print("6. List users")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_counties()
        elif choice == "2":
            add_county()
        elif choice == "3":
            list_forecasts()
        elif choice == "4":
            add_forecast()
        elif choice == "5":
            list_counties_with_forecasts()
        elif choice == "6":
            list_users()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

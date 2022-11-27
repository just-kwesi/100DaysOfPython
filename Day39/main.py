# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data = DataManager()
flight_srch = FlightSearch()
flight_price = FlightData()

# get rows of locations from google sheets using sheety.com
sheet_data = data.getFlight()

# confirm all rows include IATA codes
for flight_row in sheet_data:
    if flight_row["iataCode"] == "":
        iataCode = flight_srch.getIataCode(flight_row["city"])  # get IATA code from kiwiapi

        flight_id = flight_row["id"]  # get id for update of row

        flight_row["iataCode"] = iataCode[0]["code"]  # update row to include IATA code

        status = data.updateFlight(flight_id, flight_row)  # send a put request to update hoogle sheet

# iterate for flight prices and send sms if lesser than sheets prices
for loc in sheet_data:
    flights = flight_price.getPrices(loc["iataCode"])


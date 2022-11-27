# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from pprint import pprint
from dotenv import dotenv_values
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

CONFIG = dotenv_values('.env')

send_notification = NotificationManager(CONFIG)
data = DataManager(CONFIG)
flight_srch = FlightSearch(CONFIG)
flight_price = FlightData(CONFIG)

# get rows of locations from Google sheets using sheety.com
sheet_data = data.getFlight()

# confirm all rows include IATA codes
for flight_row in sheet_data:
    if flight_row["iataCode"] == "":
        iataCode = flight_srch.getIataCode(flight_row["city"])  # get IATA code from kiwi.api
        flight_id = flight_row["id"]  # get id for update of row
        flight_row["iataCode"] = iataCode[0]["code"]  # update row to include IATA code
        status = data.updateFlight(flight_id, flight_row)  # send a put request to update hoogle sheet


# iterate for flight prices and send sms if lesser than sheets prices
for loc in sheet_data:
    flights = flight_price.getPrices(loc)
    if flights and len(flight_price.flights):
        send_notification.sendMessages(flight_price.flights)

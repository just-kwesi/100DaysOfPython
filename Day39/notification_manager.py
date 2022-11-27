from twilio.rest import Client


def makeMessage(flight):
    price = flight["price"]
    city = flight["cityFrom"]
    iata_code = flight["cityCodeFrom"]
    city_to = flight["cityTo"]
    city_code_to = flight["cityCodeTo"]
    outbound_date = flight["route"][0]["local_departure"]
    departure_date = flight["route"][1]["local_departure"]
    booking_url = flight["deep_link"]

    message = f"Low price alert!\nPrice: {price}\nFrom: {city} - {iata_code}\nTo: {city_to} - {city_code_to}\n"
    message += f"Outbound Date: {outbound_date}\nInbound Date: {departure_date}\nBooking URL: {booking_url}"

    return message


class NotificationManager:
    def __init__(self, config):
        self.account_sid = config['TWILIO_ACCOUNT_SID']
        self.auth_token = config['TWILIO_AUTH_TOKEN']

    def sendMessages(self, flights):
        client = Client(self.account_sid, self.auth_token)

        for flight in flights:
            message = makeMessage(flight)

            message = client.messages \
                .create(
                body=message,
                from_='+15133275938',
                to='+17184154873'
            )
            response = message.error_code
            if response == None:
                continue
            else:
                break

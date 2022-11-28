from twilio.rest import Client
import smtplib
from email.message import EmailMessage


def makeMessage(flight):
    price = flight["price"]
    city = flight["cityFrom"]
    iata_code = flight["cityCodeFrom"]
    city_to = flight["cityTo"]
    city_code_to = flight["cityCodeTo"]
    booking_url = flight["deep_link"]

    route = flight["route"]
    route_len = len(route)
    outbound_date = route[0]["local_departure"].split("T")
    departure_date = route[route_len - 1]["local_departure"].split("T")

    message = f"Low price alert!\nPrice: USD{price}\nFrom: {city} - {iata_code}\nTo: {city_to} - {city_code_to}\n"
    message += f"Outbound Date: {outbound_date[0]}\nOutbound Time: {outbound_date[1][:-1]}\n"
    message += f"Inbound Date: {departure_date[0]}\nInbound Time: {departure_date[1][:-1]}\n"

    if route_len == 4:
        layover_city = route[1]["cityFrom"]
        message += f"Flight has 1 stop over, via {layover_city}."

    message += f"Booking URL: {booking_url}"

    return message


class NotificationManager:
    def __init__(self, config):
        self.account_sid = config['TWILIO_ACCOUNT_SID']
        self.auth_token = config['TWILIO_AUTH_TOKEN']
        self.email = config['EMAIL']
        self.email_password = config["EMAIL_PASSWORD"]

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
            if response is None:
                continue
            else:
                break

    def sendEmails(self, emails, flight):
        my_email = self.email
        password = self.email_password

        for email_address in emails:
            body = makeMessage(flight)

            em = EmailMessage()
            em['From'] = my_email
            em["To"] = email_address["email"]
            em["Subject"] = "Low Flight Alert"
            em.set_content(body)

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email_address["email"],
                    msg=em.as_string()
                )

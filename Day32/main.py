import random
import smtplib
import datetime as dt
import pandas as pd
from dotenv import dotenv_values
from email.message import EmailMessage


config = dotenv_values(".env")


def get_letter(name):
    birthday_wishes = []

    with open("letter_templates/letter_1.txt") as letter_one:
        birthday_mail = letter_one.read()
        birthday_wishes.append(birthday_mail)

    birthday_mail = random.choice(birthday_wishes).replace("[NAME]", name)
    return birthday_mail


# send letter with smtp

def send_letter(letter_to_send, person):
    my_email = config['EMAIL']
    password = config["PASSWORD"]

    em = EmailMessage()
    em['From'] = my_email
    em['To'] = person["email"]
    em['Subject'] = "Birthday Wishes"
    em.set_content(letter_to_send)

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person["email"],
            msg=em.as_string()
        )


# 2. Check if today matches a birthday in the birthdays.csv
dates = pd.read_csv("birthdays.csv")
dates_dict = dates.to_dict(orient="records")
today = dt.datetime.now()
day = today.day
month = today.month

for date in dates_dict:
    if date["month"] == month and date["day"] == day:
        letter = get_letter(date["name"])
        send_letter(letter, date)

# 4. Send the letter generated in step 3 to that person's email address.

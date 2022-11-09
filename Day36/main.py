import requests
from dotenv import dotenv_values
import datetime as dt
from twilio.rest import Client

config = dotenv_values(".env")

STOCK = "MSFT"
COMPANY_NAME = "Microsoft"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def stock_details(stock):
    stock_url = "https://www.alphavantage.co/query"
    stock_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": stock,
        "apikey": config['ALPHA_VANTAGE_API_KEY']
    }
    stock_response = requests.get(stock_url, params=stock_params)
    stock_response.raise_for_status()
    data = stock_response.json()["Time Series (Daily)"]

    today = dt.date.today()
    yesterday = today - dt.timedelta(days=1)
    day_before_yesterday = today - dt.timedelta(days=2)

    # stock data for yesterday and the day before
    yesterday_stock = data[yesterday.strftime('%Y-%m-%d')]
    day_before_yesterday_stock = data[day_before_yesterday.strftime('%Y-%m-%d')]

    # percentage change for the stock
    yesterday_close = float(yesterday_stock["4. close"])
    day_before_close = float(day_before_yesterday_stock['4. close'])
    net_change = (yesterday_close - day_before_close) / day_before_close * 100

    return net_change


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def getNews(company_name):
    newsapi_url = "https://newsapi.org/v2/everything"
    newsapi_params = {
        'q': company_name,
        'from': dt.date.today().strftime('%Y-%m-%d'),
        'sortBy': 'popularity',
        "apiKey": config['NEWSAPI_KEY']
    }

    news_response = requests.get(newsapi_url, params=newsapi_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]
    return news_data


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. \
percent_change = stock_details(STOCK)
stock_message_list = []
if abs(percent_change) >= 0:
    if percent_change >= 0:
        message_start = f"{STOCK}: 🔺{abs(round(percent_change, 1))}%\n\n"
    else:
        message_start = f"{STOCK}: 🔻{abs(round(percent_change, 1))}%\n\n"

    stock_message_list.append(message_start)

    news = getNews(COMPANY_NAME)
    for news_item in news:
        headline = news_item['title']
        description = news_item['description']
        source_url = news_item['url']
        news_string = f'Headline: {headline}\n\nDescription: {description}\n\nSource URL: {source_url}\n\n\n'
        stock_message_list.append(news_string)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config['TWILIO_ACCOUNT_SID']
auth_token = config['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message_body = ''.join(stock_message_list)
message = client.messages \
    .create(
    body=message_body,
    from_='+15133275938',
    to='+17184154873'
)

message.sid

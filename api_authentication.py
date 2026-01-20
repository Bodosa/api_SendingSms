"""
API Key = like the personal number or password
This is the way how the API provider can track how much you're using their API
and to authorize your access and deny your access once you've gone over the limit.

Different API providers tend to have different was that you can authenticate with them

"""
import requests
from twilio.rest import Client
import os

# !!! Free API key!!!
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_key = os.environ.get("OWM_API_KEY")

# my own id & token from free twilio account
account_sid = "ACc9ba92c3cf418b2ef06eb4578912f971"
auth_token = os.environ.get("AUTH_TOKEN")

# long, lat need to be changed based on condition code
# if <700 (rain, snow,..) you need to change long,lat where it can rain,.. and vise versa
weather_params = {
    "lat": 48.208176,
    "lon": 16.373819,
    "appid": API_key,
    "cnt": 4,
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
# print(data["list"][0]["weather"][0]["id"])

will_sunny = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_sunny = True
if will_sunny:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's sunny today. Have a great day!!!!",
        from_="+17658856122",
        # your verified number
        to="+421944365972",
    )
    print(message.status)


"""
Environment variables = terminal (git bash) -> env = whole bunch of variables 
= system-level variables used to store configuration values outside of source code (passwords, API key,..)
it's used for security, configuration and convenience
use: with library os 
1. import os
2. (terminal bash) export OWM_API_KEY="value"
3. (15. row) API_key = os.environ.get("OWM_API_KEY")
4. (terminal bash) python api_authentication.py 


"""
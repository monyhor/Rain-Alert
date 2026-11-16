import requests
import os
import smtplib
MY_LAT = 11.556374
MY_LONG = 104.928207
MY_API_KEY = os.environ.get("OWM_API")
MY_PASS = os.environ.get("MY_PASSWORD")
parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "cnt" : 4,
    "appid" : MY_API_KEY
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status()
data = response.json()['list']

listofWeather = [item['weather'][0] for item in data]
willRain = False
for item in listofWeather:
    if item['id'] < 700:
        willRain = True
if willRain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL , MY_PASS)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = RECEIVER_EMAIL,
            msg = "Subject: Weather is Rainy!\n\n"
                "Please bring your umbrella!"
        )





import requests
import json
import pyttsx3
text_to_speech = pyttsx3.init()
text_to_speech.say(f"Enter the name of city")
text_to_speech.runAndWait()
city=input("Enter the name of city:\n")
url=f"https://api.weatherapi.com/v1/current.json?key=2ddbcf535d23486e8c1133428230404&q={city}"
r=requests.get(url)
#print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
a=wdic["location"]["region"]
b=wdic["current"]["last_updated"]
c=wdic["current"]["wind_kph"]
text_to_speech.say(f"The temperature of {city} is {w} degrees.")
text_to_speech.say(f"It is located in {a}")
text_to_speech.say(f"Current wind speed is {c} in {city}")
text_to_speech.say(f"Last updated time was {b}")
text_to_speech.runAndWait()
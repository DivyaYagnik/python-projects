import requests 

city = input("Enter city name: ")

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=APIKEY".format(city)

res = requests.get(url).json()

temperature = res['main']['temp']

print(temperature)
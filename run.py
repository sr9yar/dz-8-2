from requests import get
from json import loads
from sys import exit



API_KEY = "c907f5cb2617b8dcdcb46679f337a2ad"



def get_weather_url(lat: str, lon: str):
  return f"https://api.openweathermap.org/data/2.5/weather?units=metric&lat={lat}&lon={lon}&appid={API_KEY}"



def get_weather(city: str):

  if not city:
    print(f"\nГород не был указан.")
    exit(0)

  try:
    res = get(f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}")
    resBody = loads(res.text)
  except:
    print(f"\nНе удалось получить координаты для города {city}")
    exit(0)

  lat = resBody[0]["lat"]
  lon = resBody[0]["lon"]

  try:
    response = get(get_weather_url(lat, lon))
    body = loads(response.text)
  except:
    print(f"\nНе удалось получить данные по погоде для {city}")
    exit(0)

  return body



def main():
  if not API_KEY:
    print(f"\nОтсутсвует ключ АПИ.")
    exit(0)

  city = input("Введите название города: ")

  data = get_weather(city)

  print(f"Температура: {data["main"]["temp"]}°C")
  print(f"\nОписание погоды: {data["weather"][0]["description"]}")



main()



from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather(city):
    obs = mgr.weather_at_place(city)
    w = obs.weather
    return f"Weather in {city}:\n" \
           f"Status: {w.detailed_status}\n" \
           f"Temperature: {w.temperature('celsius')['temp']}°C\n" \
           f"Humidity: {w.humidity}%\n" \
           f"Wind Speed: {w.wind()['speed']} m/s\n"


# Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place('London,GB')
# w = observation.weather
#
# print(w.detailed_status)  # 'clouds'
# print(w.wind())  # {'speed': 4.6, 'deg': 330}
# print(w.humidity)  # 87
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print(w.rain)  # {}
# print(w.heat_index)  # None
# print(w.clouds)  # 75

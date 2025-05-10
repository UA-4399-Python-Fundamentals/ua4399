from pyowm import OWM


API_KEY = 'key'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

city = "Lviv,UA"

observation = mgr.weather_at_place(city)
print(observation.weather)
w = observation.weather

# weather_info = (
#     f"Status: {w.detailed_status}\n"
#     f"Wind: {w.wind()}\n"
#     f"Humidity: {w.humidity}\n"
#     f"Temperature: {w.temperature('celsius')}\n"
#     f"Rain: {w.rain}\n"
#     f"Heat Index: {w.heat_index}\n"
#     f"Clouds: {w.clouds}"
# )
weather_info = {
    "Status": w.detailed_status,
    "Wind": w.wind(),
    "Humidity": w.humidity,
    "Temperature": w.temperature('celsius'),
    "Rain": w.rain,
    "Heat Index": w.heat_index,
    "Clouds": w.clouds,
}
from pprint import pprint
pprint(weather_info)
print(observation)
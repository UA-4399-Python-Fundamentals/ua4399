from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city):
    # The following lines may raise exceptions if the city is invalid or network is unavailable
    observation = mgr.weather_at_place(city)
    w = observation.weather

    result = f"Status: {w.detailed_status}\n"
    result += f"Wind: {w.wind()}\n"
    result += f"Humidity: {w.humidity}\n"
    result += f"Temperature: {w.temperature('celsius')}\n"
    result += f"Rain: {w.rain}\n"
    result += f"Heat index: {w.heat_index}\n"
    result += f"Clouds: {w.clouds}"

    return result




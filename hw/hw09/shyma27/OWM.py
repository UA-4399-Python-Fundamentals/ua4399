from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather(location):
    '''Get weather details based on location'''
    observation = mgr.weather_at_place(location)
    w = observation.weather
    return w

    #return w.detailed_status, w.wind(), w.humidity, w.temperature('celsius'), w.rain, w.heat_index, w.clouds
    # print(w.detailed_status)         # 'clouds'
    # print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    # print(w.humidity)                # 87
    # print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # print(w.rain)                    # {}
    # print(w.heat_index)              # None
    # print(w.clouds)                  # 75






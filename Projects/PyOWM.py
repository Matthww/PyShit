import pyowm

owm = pyowm.OWM('797153f746aae22307499da4ad723468')

observation = owm.weather_at_place('Almere,nl')
w = observation.get_weather()
print(w)

wind = w.get_wind()
temp = w.get_temperature('celsius')
print(wind)
print(temp)

observation_list = owm.weather_around_coords(52.371353, 5.222124)
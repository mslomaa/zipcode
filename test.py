import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

geolocator = Nominatim(user_agent="specify_your_app_name_here")
location2 = geolocator.geocode('Warszawa')
loc2 = location2.latitude, location2.longitude

print(loc2)
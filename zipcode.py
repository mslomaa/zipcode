import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

# biedronka = pandas.read_excel(r'//home/sloma/Desktop/biedra/testbiedra.xlsx', usecols="A, B, C, H, I")
biedronka = pd.ExcelFile(r'//home/sloma/Desktop/biedra/testbiedra.xlsx').parse('Arkusz1')

x = []
worker = []
x.append((biedronka[['Adres zamieszkania', 'Miasto']]))

for z in x:
    city = z['Miasto']
    adress = z['Adres zamieszkania']
    city += ' ' + adress
    worker.append(city)

coordinates = []
for k in worker:
    for i in k:
        try:
            geolocator = Nominatim(user_agent="specify_your_app_name_here")
            location = geolocator.geocode(i)
            location = location.latitude, location.longitude
            coordinates.append(location)
        except AttributeError:
            coordinates.append('NaN')
            continue

# //problem z czytaniem wspolrzednych z listy
# dist = []
#
# for loc in coordinates:
#     try:
#
#         miasto1 = loc
#         miasto2 = loc2
#         dist = great_circle(miasto1, miasto2).kilometers
#     except AttributeError:
#         dist.append('NaN')
#         continue
#
#
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
# location2 = geolocator.geocode('Warszawa')
# loc2 = location2.latitude, location2.longitude


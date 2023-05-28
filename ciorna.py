import requests
import datetime as dt
#
#
# respone = requests.get(url='http://api.open-notify.org/iss-now.json')
#
# respone.raise_for_status()
#
# data = respone.json()
# longitudinea = data['iss_position']['longitude']
# latitudinea = data['iss_position']['latitude']
#
# iss_position = (longitudinea, latitudinea)
# print(iss_position)

LAT: float = 46.770920
LNG: float = 23.589920
parameters = {
    'lat': LAT,
    'lng': LNG,
    'date': f'{dt.datetime.now().year}-{dt.datetime.now().month}-{dt.datetime.now().day}',
    'formatted': 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
rasarit: str = data['results']['sunrise']
apus = data['results']['sunset']


print(rasarit.split('T')[-1].split(':')[0])



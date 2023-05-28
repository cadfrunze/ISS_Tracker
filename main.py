# Urmarirea, localizarea obiectului (ISS)
from functionalitati import *
from time import sleep


def localizare():
    """Urmarire, localizare ISS daca este in apropiere de utilizator"""
    iss_lat: float = lat_iss()
    iss_lng: float = lng_iss()
    ora_user: int = timp_user()['ora']
    rasarit: int = rasarit_user()
    apus: int = apus_user()

    while (iss_lat - USER_LAT < 0 or iss_lat - USER_LAT > 5) or (iss_lng - USER_LNG < 0 or iss_lng - USER_LNG > 5):
        iss_lat: float = lat_iss()
        iss_lng: float = lng_iss()
        print(f'lat_iss: {iss_lat}, lng_iss: {iss_lng}')
        sleep(1)
    else:
        print('este in apropiere')
        if (ora_user >= apus) or (ora_user < rasarit):
            print('te poti uita pe cer')
        else:
            localizare()


if '__main__' == __name__:
    localizare()

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

    while True:
        if (iss_lat - USER_LAT >= 0 or iss_lat - USER_LAT <= 5) and (
                iss_lng - USER_LNG >= 0 or iss_lng - USER_LNG <= 5) and (ora_user >= apus) or (ora_user < rasarit):
            pass
        print(f'lat_iss: {iss_lat}, lng_iss: {iss_lng}, ora mea: {ora_user}, rasarit: {rasarit}, apus: {apus}')
        print(f"Latitudine apropiere: {iss_lat - USER_LAT}, Longitudine apropiere: {iss_lng - USER_LNG}")
        iss_lat: float = lat_iss()
        iss_lng: float = lng_iss()
        ora_user: int = timp_user()['ora']
        rasarit: int = rasarit_user()
        apus: int = apus_user()
        sleep(1)


if '__main__' == __name__:
    localizare()

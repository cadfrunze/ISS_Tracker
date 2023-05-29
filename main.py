# Urmarirea, localizarea obiectului (ISS)
from functionalitati import *
import time


def localizare():
    """Urmarire, localizare ISS daca este in apropiere de utilizator"""
    iss_lat: float = round(lat_iss(), 2)
    iss_lng: float = round(lng_iss(), 2)
    ora_user: int = timp_user()['ora']
    rasarit: int = rasarit_user()
    apus: int = apus_user()

    while True:
        print(f'lat_iss: {iss_lat}, lng_iss: {iss_lng}, ora mea: {ora_user}, rasarit: {rasarit}, apus: {apus}')
        print(f"Latitudine apropiere: {round(iss_lat - USER_LAT, 2)}, Longitudine apropiere: {round(iss_lng - USER_LNG, 2)}")
        if (iss_lat - USER_LAT > 0 and iss_lat - USER_LAT <= 5) and (
                iss_lng - USER_LNG > 0 and iss_lng - USER_LNG <= 5) and ((ora_user >= apus) or (ora_user < rasarit)):
            # send_email(ora_adevar=ora_user)
            print('am intrat')
            break

        iss_lat: float = round(lat_iss(), 2)
        iss_lng: float = round(lng_iss(), 2)
        ora_user: int = timp_user()['ora']
        rasarit: int = rasarit_user()
        apus: int = apus_user()
        time.sleep(5)


if '__main__' == __name__:
    localizare()

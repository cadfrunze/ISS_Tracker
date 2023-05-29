# Creeare, preluare date
import requests
from datetime import datetime
import smtplib

USER_LAT: float = 46.770920
USER_LNG: float = 23.589920

USER_EMAIL = 'test@test.test'
USER_PASS = '123test_'


# Creearea API-uri

def lat_iss() -> float:
    """Returnarea valorii de tip float a latitudinii ISS """
    raspuns = requests.get('http://api.open-notify.org/iss-now.json')
    raspuns.raise_for_status()
    data: dict = raspuns.json()
    return float(data['iss_position']['latitude'])


def lng_iss() -> float:
    """Returnarea valorii de tip float a longitudinii ISS """
    raspuns = requests.get('http://api.open-notify.org/iss-now.json')
    raspuns.raise_for_status()
    data: dict = raspuns.json()
    return float(data['iss_position']['longitude'])


# Timp
def timp_user() -> dict:
    """Returnarea zi, luna, an, ora (format 24) de tip dict in timp real al utilizatorului"""
    return {
        'an': int(datetime.now().year),
        'luna': int(datetime.now().month),
        'zi': int(datetime.now().day),
        'ora': int(datetime.now().hour)
    }


def rasarit_user() -> int:
    """Returnarea valorii in timp real de tip int orei rasarit utilizator"""
    user_timp: dict = timp_user()
    parametrii = {
        'lat': USER_LAT,
        'lng': USER_LNG,
        'date': f'{user_timp["an"]}-{user_timp["luna"]}-{user_timp["zi"]}',
        'formatted': 0
    }
    raspuns = requests.get('https://api.sunrise-sunset.org/json', params=parametrii)
    raspuns.raise_for_status()
    data = raspuns.json()
    return int(data['results']['sunrise'].split('-')[-1].split('T')[-1].split(':')[0])


def apus_user() -> int:
    """Returnarea valorii in timp real de tip int orei apus utilizator"""
    user_timp: dict = timp_user()
    parametrii = {
        'lat': USER_LAT,
        'lng': USER_LNG,
        'date': f'{user_timp["an"]}-{user_timp["luna"]}-{user_timp["zi"]}',
        'formatted': 0
    }
    raspuns = requests.get('https://api.sunrise-sunset.org/json', params=parametrii)
    raspuns.raise_for_status()
    data = raspuns.json()
    return int(data['results']['sunset'].split('-')[-1].split('T')[-1].split(':')[0])


def send_email(ora_adevar):
    """Transmitere date, anuntarea utilizatorului prin email la aparitia ISS pe cer, conform cerintelor"""
    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=USER_PASS)
        connection.sendmail(from_addr=USER_EMAIL,
                            to_addrs='test@test.test',
                            msg=f'Subject: Uitate la cer!\\n{ora_adevar}')


from datetime import datetime

astazi = datetime.now()
with open('./work_log.txt', 'a') as innregistrare:
    innregistrare.writelines(f"Data: {astazi.day}/{astazi.month}/{astazi.year} | Ora: {astazi.hour}:{astazi.minute}\n")
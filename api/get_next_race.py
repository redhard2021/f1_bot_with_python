from api.client import get_races
from datetime import datetime
import pytz

def get_next_race():
    races = get_races()
    next_race = bring_next_f1_race(races)
    if next_race is not None:
        converted_race_date = convert_utc_to_buenos_aires(next_race['date'], next_race['time'])
        converted_practice_date = convert_utc_to_buenos_aires(next_race['FirstPractice']['date'],next_race['FirstPractice']['time'])
        converted_qualifying_date = convert_utc_to_buenos_aires(next_race['Qualifying']['date'],next_race['Qualifying']['time'])

        return f"Fecha: {converted_race_date.strftime("%d/%m")} \nCircuito: {next_race['Circuit']['circuitName']}. \n\nHorarios (Argentina):\nPractica 1: {converted_practice_date.strftime("%H:%M")}hrs.\nQualy: {converted_qualifying_date.strftime("%H:%M")}hrs.\nCarrera: {converted_race_date.strftime("%H:%M")}hrs.\n"
        
        

def bring_next_f1_race(races):
    today = datetime.now()
    next_race = None
    for race in races:
        incoming_date = datetime.strptime(race["date"], "%Y-%m-%d")
        if incoming_date > today:
            next_race = race
            break
    return next_race


def convert_utc_to_buenos_aires(date_str, time_str):
   datetime_str = f"{date_str}T{time_str}"
   utc_time = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
   buenos_aires_timezone = pytz.timezone('America/Argentina/Buenos_Aires')
   buenos_aires_time = utc_time.astimezone(buenos_aires_timezone)
   return buenos_aires_time

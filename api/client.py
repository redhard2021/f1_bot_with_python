import requests


def get_races():
    url = "https://api.jolpi.ca/ergast/f1/2025/races/"
    response = requests.get(url)
    data = response.json()

    return data['MRData']['RaceTable']['Races']



def get_driver_standings():
    url = "https://api.jolpi.ca/ergast/f1/2025/driverstandings/"
    response = requests.get(url)
    data = response.json()

    return data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

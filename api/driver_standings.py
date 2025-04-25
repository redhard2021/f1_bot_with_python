from api.client import get_driver_standings

def driver_standings():
    driver_standings = get_driver_standings()
    if driver_standings is not None:
        result = "Posición | Piloto | Puntos\n"
        result += "--------|--------|-------\n"
        for standing in driver_standings:
            position = standing['position']
            driver_name = f"{standing['Driver']['givenName']} {standing['Driver']['familyName']}"
            points = standing['points']
            result += f"{position} | {driver_name} | {points}\n"
        return result
    
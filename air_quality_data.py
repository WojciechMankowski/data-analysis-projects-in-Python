from datetime import datetime

import requests

# URL API
BASE_URL = "https://api.gios.gov.pl/pjp-api/rest/"


def get_stations():
    """Pobiera listę stacji pomiarowych."""
    url = BASE_URL + "station/findAll"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_sensors(station_id):
    """Pobiera listę stanowisk pomiarowych dla danej stacji."""
    url = BASE_URL + f"station/sensors/{station_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_data(sensor_id):
    """Pobiera dane historyczne dla danego stanowiska pomiarowego."""
    size = datetime.now().hour
    url = BASE_URL + f"data/getData/{sensor_id}?size={size}&sort=Data"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_archival_data(sensor_id):
    """Pobiera dane archiwalne dla danego stanowiska pomiarowego."""
    days = (datetime.now() - datetime(2024, 1, 1)).days
    url = BASE_URL + f"archivalData/getDataBySensor/{sensor_id}?size=500&dayNumber={1}"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()["Lista archiwalnych wyników pomiarów"]


def main():
    # Pobierz listę stacji pomiarowych
    stations = get_stations()

    # Wybierz pierwszą stację (dla przykładu)
    station_id = stations[0]["id"]
    station_name = stations[0]["stationName"]
    print(f"Wybrana stacja: {station_name} (ID: {station_id})")

    # Pobierz listę stanowisk pomiarowych dla wybranej stacji
    sensors = get_sensors(station_id)
    for sensor in sensors:
        print(sensor)
    # Wybierz pierwsze stanowisko pomiarowe (dla przykładu)
    sensor_id = sensors[0]["id"]
    sensor_param = sensors[0]["param"]["paramName"]
    print(f"Wybrane stanowisko: {sensor_param} (ID: {sensor_id})")


if __name__ == "__main__":
    main()

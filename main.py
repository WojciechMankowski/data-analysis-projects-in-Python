from time import sleep, time

from database import AirQualityDatabase
from air_quality_data import *


def main():
    start_time = time()
    db = AirQualityDatabase()
    largest_cities_poland = [
        "Warszawa",
        "Kraków",
        "Łódź",
        "Wrocław",
        "Poznań",
        "Gdańsk",
        "Szczecin",
        "Bydgoszcz",
        "Lublin",
        "Białystok",
    ]
    # my_city = largest_cities_poland[9]
    stations_id = []
    sensors = []

    # pobranie id stacji
    # for item in db.get_id("Station"):
    #     stations_id.append(item[0])

    for stations in db.get_data("Station"):
        if stations[4] in largest_cities_poland:
            stations_id.append(stations[0])

    # pobranie id sensora
    # for ids in db.get_data("Sensors"):
    #     # print(ids)
    #     station_id = ids[1]
    #     if station_id in stations_id:
    #         # pobranie danych historycznych
    #         for item in get_archival_data(ids[0]):
    #             db.add_archival_data(
    #                 name=item["Nazwa stacji"],
    #                 stationCode=item["Kod stanowiska"],
    #                 date=item["Data"],
    #                 value=item["Wartość"],
    #             )
    #             sleep(5)
    indeks = 0
    for ids in db.get_data("Sensors"):
        data = get_data(ids[0])
        key = data["key"]
        values = data["values"]

        for item in values:
            db.add_air_quality_data(key, item["date"], item["value"], ids[0])
        end_time = time()
        elapsed_time = end_time - start_time
        print(f"Czas wykonania pętli for: {elapsed_time} sekundy")
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Czas wykonania całego programu: {elapsed_time} sekundy")


if __name__ == "__main__":
    main()

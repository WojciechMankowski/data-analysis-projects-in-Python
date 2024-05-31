from sqlite3 import connect


class AirQualityDatabase:
    def __init__(self, db_name="air_quality.db"):
        self.db_name = db_name
        self.conn = connect(self.db_name)
        self.cursor = self.conn.cursor()

    def add_station(self, data):
        self.cursor.execute(
            """
            INSERT INTO Station (id, stationName, gegrLat, gegrLon, cityName, communeName, districtName, provinceName, addressStreet)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["id"],
                data["stationName"],
                data["gegrLat"],
                data["gegrLon"],
                data["city"]["name"],
                data["city"]["commune"]["communeName"],
                data["city"]["commune"]["districtName"],
                data["city"]["commune"]["provinceName"],
                data.get("addressStreet"),
            ),
        )
        self.conn.commit()

    def add_archival_data(self, name, stationCode, date, value):
        self.cursor.execute(
            """
            SELECT * FROM Archived_data 
            WHERE stationName = ? AND date = ? AND value = ?
            """,
            (name, date, value),
        )
        existing_data = self.cursor.fetchone()
        if not existing_data:
            self.cursor.execute(
                """
                INSERT INTO Archived_data (stationName, stationCode, date, value)
                VALUES (?, ?, ?, ?)
                """,
                (name, stationCode, date, value),
            )
            self.conn.commit()

    def add_sensor(self, data):
        conn = connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO Sensors (id, stationId, paramName, paramFormula, paramCode, idParam)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                data["id"],
                data["stationId"],
                data["param"]["paramName"],
                data["param"]["paramFormula"],
                data["param"]["paramCode"],
                data["param"]["idParam"],
            ),
        )
        conn.commit()
        conn.close()

    def get_data(self, name_table):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SELECT * FROM {name_table}")
        return self.cursor.fetchall()

    def get_id(self, name_table):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SELECT Id FROM {name_table}")
        return self.cursor.fetchall()

    def add_air_quality_data(self, key, date, value, sensor_id):
        self.cursor.execute(
            """
            INSERT INTO air_quality (pollutant, measurement_date, value,sensor_id)
            VALUES (?, ?, ?, ?)
            """,
            (key, date, value, sensor_id),
        )

        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

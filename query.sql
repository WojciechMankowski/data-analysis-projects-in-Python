CREATE TABLE Archived_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stationName TEXT,
    stationCode TEXT,
    date TEXT,
    value REAL)

CREATE TABLE Sensors (
    id INT PRIMARY KEY,
    stationId INT,
    paramName VARCHAR(255),
    paramFormula VARCHAR(10),
    paramCode VARCHAR(10),
    idParam INT,
    FOREIGN KEY (stationId) REFERENCES Station(id)
);

CREATE TABLE air_quality (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pollutant TEXT,
    measurement_date TEXT,
    value REAL,
    sensor_id INTEGER,
    FOREIGN KEY (sensor_id) REFERENCES Sensors(id)
);


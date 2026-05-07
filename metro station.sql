CREATE DATABASE mydb;
USE mydb;

CREATE TABLE Stations(
    station_id INT PRIMARY KEY,
    station_name VARCHAR(50),
    location VARCHAR(50),
    platforms INT
);

CREATE TABLE Metro_Trains(
    train_id INT PRIMARY KEY,
    train_name VARCHAR(50),
    capacity INT,
    station_id INT,
    FOREIGN KEY (station_id) REFERENCES Stations(station_id)
);

ALTER TABLE Stations
ADD opening_year INT;

ALTER TABLE Metro_Trains
RENAME TO Trains;

INSERT INTO Stations VALUES(1,'Central','Downtown',4,2005);
INSERT INTO Stations VALUES(2,'Green Park','North',3,2010);
INSERT INTO Stations VALUES(3,'Lake View','East',2,2012);
INSERT INTO Stations VALUES(4,'Airport','Airport Road',5,2018);
INSERT INTO Stations VALUES(5,'City Mall','West',3,2015);

INSERT INTO Trains VALUES(101,'Metro Express',800,1);
INSERT INTO Trains VALUES(102,'City Rapid',750,2);
INSERT INTO Trains VALUES(103,'Airport Link',900,4);

UPDATE Trains
SET capacity = 850
WHERE train_id = 102;

DELETE FROM Stations
WHERE station_id = 3;

SELECT * FROM Stations;
SELECT * FROM Trains;

CREATE USER 'metro_staff'@'localhost' IDENTIFIED BY 'password123';

GRANT SELECT ON mydb.Stations TO 'metro_staff'@'localhost';
GRANT INSERT ON mydb.Trains TO 'metro_staff'@'localhost';

REVOKE INSERT ON mydb.Trains FROM 'metro_staff'@'localhost';
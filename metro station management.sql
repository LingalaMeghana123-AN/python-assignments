-- Create and select database
CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

-- DDL: Create tables
CREATE TABLE IF NOT EXISTS Stations(
    station_id INT PRIMARY KEY,
    station_name VARCHAR(50),
    location VARCHAR(50),
    platforms INT
);

CREATE TABLE IF NOT EXISTS Metro_Trains(
    train_id INT PRIMARY KEY,
    train_name VARCHAR(50),
    capacity INT,
    station_id INT,
    FOREIGN KEY (station_id) REFERENCES Stations(station_id)
);

-- Modify Stations table
ALTER TABLE Stations
ADD COLUMN IF NOT EXISTS opening_year INT;

-- Rename Metro_Trains to Trains
RENAME TABLE Metro_Trains TO Trains;

-- DML: Insert stations
INSERT INTO Stations VALUES
(1,'Central','Downtown',4,2005),
(2,'Green Park','North',3,2010),
(3,'Lake View','East',2,2012),
(4,'Airport','Airport Road',5,2018),
(5,'City Mall','West',3,2015);

-- Insert trains
INSERT INTO Trains VALUES
(101,'Metro Express',800,1),
(102,'City Rapid',750,2),
(103,'Airport Link',900,4);

-- Update train capacity
UPDATE Trains
SET capacity = 850
WHERE train_id = 102;

-- Delete a station closed for maintenance
DELETE FROM Stations
WHERE station_id = 3;

-- Display all data
SELECT * FROM Stations;
SELECT * FROM Trains;

-- DCL: User access control
CREATE USER IF NOT EXISTS 'metro_staff'@'localhost' IDENTIFIED BY 'password123';

GRANT SELECT ON mydb.Stations TO 'metro_staff'@'localhost';
GRANT INSERT ON mydb.Trains TO 'metro_staff'@'localhost';

REVOKE INSERT ON mydb.Trains FROM 'metro_staff'@'localhost';

FLUSH PRIVILEGES;
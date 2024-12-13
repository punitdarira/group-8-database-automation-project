CREATE TABLE ClimateData (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    temperature FLOAT NOT NULL,
    precipitation FLOAT NOT NULL
);

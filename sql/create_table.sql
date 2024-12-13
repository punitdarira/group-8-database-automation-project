CREATE TABLE ClimateData (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    temperature FLOAT NOT NULL
);

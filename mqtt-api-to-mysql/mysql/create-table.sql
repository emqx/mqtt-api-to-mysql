
CREATE DATABASE IF NOT EXISTS `temp_data` CHARACTER SET utf8mb4;

USE `temp_data`;

CREATE TABLE IF NOT EXISTS temp_data_events (
        id INT AUTO_INCREMENT PRIMARY KEY,
        clientid VARCHAR(255),
        event VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE IF NOT EXISTS temp_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        device_id VARCHAR(50),
        temperature FLOAT NOT NULL,
        humidity FLOAT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );%   

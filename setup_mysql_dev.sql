-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS qm_dev_db;
CREATE USER IF NOT EXISTS 'qm_dev'@'localhost' IDENTIFIED BY 'qm_dev_pwd';
GRANT ALL PRIVILEGES ON `qm_dev_db`.* TO 'qm_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'qm_dev'@'localhost';
FLUSH PRIVILEGES;

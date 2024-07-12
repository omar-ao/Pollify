-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS qm_test_db;
CREATE USER IF NOT EXISTS 'qm_test'@'localhost' IDENTIFIED BY 'qm_test_pwd';
GRANT ALL PRIVILEGES ON `qm_test_db`.* TO 'qm_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'qm_test'@'localhost';
FLUSH PRIVILEGES;

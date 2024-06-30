-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS pollify_dev_db;
CREATE USER IF NOT EXISTS 'pollify_dev'@'localhost' IDENTIFIED BY 'pollify_dev_pwd';
GRANT ALL PRIVILEGES ON `pollify_dev_db`.* TO 'pollify_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'pollify_dev'@'localhost';
FLUSH PRIVILEGES;

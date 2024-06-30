-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS pollify_test_db;
CREATE USER IF NOT EXISTS 'pollify_test'@'localhost' IDENTIFIED BY 'pollify_test_pwd';
GRANT ALL PRIVILEGES ON `pollify_test_db`.* TO 'pollify_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'pollify_test'@'localhost';
FLUSH PRIVILEGES;

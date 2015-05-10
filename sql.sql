create database blog1;
use blog1;
CREATE USER 'blog1'@'localhost' IDENTIFIED BY 'blog1';
GRANT ALL PRIVILEGES ON blog1.* TO 'blog1'@'localhost' WITH GRANT OPTION;

CREATE USER 'blog1'@'%' IDENTIFIED BY 'blog1';
GRANT ALL PRIVILEGES ON blog1.* TO 'blog1'@'%' WITH GRANT OPTION;

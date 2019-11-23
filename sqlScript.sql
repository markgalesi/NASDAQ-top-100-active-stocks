CREATE DATABASE demo;
USE demo;
CREATE TABLE Nasdaq(
timeCheck varchar(255),
exchangee varchar(255),
symbol varchar(255),
company varchar(255),
volume bigint,
price double,
changee double,
PRIMARY KEY (symbol));
CREATE TABLE ADMINISTRATOR (
	ID INT(11) NOT NULL AUTO_INCREMENT,
	USERNAME VARCHAR(50) NOT NULL,
    PASSWORD VARCHAR(50) NOT NULL,
	EMAIL VARCHAR(100) NOT NULL,
	ACTIVE BOOLEAN DEFAULT 1,
	PRIMARY KEY (ID)
);
BEGIN TRANSACTION;
CREATE TABLE administrator (
	admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
	fullname VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	user_role INTEGER(10) NOT NULL
);




CREATE TABLE projects (
	project_id INTEGER PRIMARY KEY AUTOINCREMENT,
	project_name VARCHAR(255) NOT NULL,
	project_description TEXT NOT NULL,
	tasks_id VARCHAR(255) NOT NULL
);


INSERT INTO "projects" VALUES(1,'MICE Project','Meetings, incentives, conference and meetings','[1,2,3,10,14,15]');



INSERT INTO "administrator" VALUES(1,'Sandy Goreraza','sandygoreraza@hotmail.com','pass123',1);
INSERT INTO "administrator" VALUES(2,'Sandy Gore','sandygore@hotmail.com','pass12345',2);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('users',6);
INSERT INTO "sqlite_sequence" VALUES('administrator',2);
INSERT INTO "sqlite_sequence" VALUES('tasks',16);
CREATE TABLE tasks (
	task_id INTEGER PRIMARY KEY AUTOINCREMENT,
	task_name VARCHAR(255) NOT NULL,
	description VARCHAR(255) NOT NULL,
	timestamp  VARCHAR(255) NOT NULL,
	user_id INTEGER(255) NOT NULL  
	);
INSERT INTO "tasks" VALUES(1,'Creates Admin Interface','Create Admin Interface - Project 2 on pirple.com','2021-07-26 16:38:30.154562',3);
INSERT INTO "tasks" VALUES(2,'Create Homework #5','Create Homework #5 on pirple.com','2021-07-24 16:38:30.154562',1);
INSERT INTO "tasks" VALUES(3,'Create Homework #4','Create Homework #4 on pirple.com','2021-07-24 16:31:30.154562',1);
INSERT INTO "tasks" VALUES(10,'sandy goreraza tasks','sandy goreraza tasks','2021-07-30 00:07:59.495955',5);
INSERT INTO "tasks" VALUES(14,'test','test','2021-08-07 23:22:57.765950',2);
INSERT INTO "tasks" VALUES(15,'mcdonalds','wdwdwfefwf','2021-08-07 23:25:25.299727',2);
INSERT INTO "tasks" VALUES(16,'ascac','acsacsacasc','2021-08-07 23:28:39.046675',5);
CREATE TABLE users (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	fullname VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL
, timestamp VARCHAR(255) NULL);
INSERT INTO "users" VALUES(1,'sandy','sandy@ztazim.co.zw','12345','2021-07-25 22:31:30.154562');
INSERT INTO "users" VALUES(2,'Sandy','gorerazasandy10@gmail.com','password','2021-07-26 22:00:30.154562');
INSERT INTO "users" VALUES(3,'test','@test','password','2021-07-26 21:00:30.154562');
INSERT INTO "users" VALUES(5,'amanda j','amanda@gmail.com','amanda','2021-07-29 23:06:56.183589');
COMMIT;

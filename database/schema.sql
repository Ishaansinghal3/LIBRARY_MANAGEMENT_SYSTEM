-- The Book Worm — Library Management System
-- Database schema (matches what Tables.py creates automatically on first run)

CREATE DATABASE IF NOT EXISTS project;
USE project;

CREATE TABLE IF NOT EXISTS BookRecord (
    BookID     VARCHAR(10) PRIMARY KEY,
    BookName   VARCHAR(35),
    Author     VARCHAR(30),
    Publisher  VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS UserRecord (
    UserID     VARCHAR(10) PRIMARY KEY,
    UserName   VARCHAR(20),
    Password   VARCHAR(20),
    BookID     VARCHAR(10),
    FOREIGN KEY (BookID) REFERENCES BookRecord(BookID)
);

CREATE TABLE IF NOT EXISTS AdminRecord (
    AdminID    VARCHAR(10) PRIMARY KEY,
    Password   VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Feedback (
    Feedback   VARCHAR(100) PRIMARY KEY,
    Rating     VARCHAR(10)
);

-- Optional seed/test data (matches Tables.py) -------------------------------

INSERT INTO UserRecord (UserID, UserName, Password, BookID) VALUES
('101', 'Kunal', '1234', NULL),
('102', 'Vishal', '3050', NULL),
('103', 'Siddhesh', '5010', NULL);

INSERT INTO AdminRecord (AdminID, Password) VALUES
('Kunal1020', '123'),
('Siddesh510', '786'),
('Vishal305', '675');

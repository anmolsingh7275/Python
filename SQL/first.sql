CREATE DATABASE CollegeDB;

USE CollegeDB;

CREATE TABLE Students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50),
    marks INT
);

INSERT INTO Students (name, age, course, marks)
VALUES 
('Anmol', 21, 'BCA', 85),
('Rahul', 22, 'BTech', 90),
('Priya', 20, 'BSc', 88);

SELECT * FROM Students;

SELECT name, marks FROM Students;

SELECT * FROM Students WHERE marks > 85;

UPDATE Students
SET marks = 95
WHERE name = 'Anmol';

DELETE FROM Students
WHERE name = 'Rahul';
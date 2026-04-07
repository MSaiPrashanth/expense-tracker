create database exp_db;
use exp_db;

create table expenses(
	id int auto_increment primary key,
    category varchar(20),
    amount float);
    
    
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);
INSERT INTO categories (name)
VALUES ('Food'), ('Travel'), ('Shopping'), ('Bills'), ('Entertainment'), ('Others');

select * from expenses;
truncate expenses;

ALTER TABLE expenses ADD COLUMN date TEXT;
INSERT INTO expenses (category, amount, date) VALUES
('Food', 250, '2024-01-05'),
('Travel', 1200, '2024-01-10'),
('Shopping', 800, '2024-01-15'),
('Bills', 1500, '2024-01-20'),
('Entertainment', 600, '2024-01-25'),

('Food', 300, '2024-02-03'),
('Travel', 900, '2024-02-08'),
('Shopping', 700, '2024-02-12'),
('Bills', 1600, '2024-02-18'),
('Others', 400, '2024-02-22'),

('Food', 350, '2024-03-02'),
('Travel', 1100, '2024-03-07'),
('Shopping', 950, '2024-03-14'),
('Bills', 1400, '2024-03-19'),
('Entertainment', 500, '2024-03-25'),

('Food', 400, '2024-04-05'),
('Travel', 1000, '2024-04-10'),
('Shopping', 850, '2024-04-15'),
('Bills', 1550, '2024-04-20'),
('Others', 450, '2024-04-28'),

('Food', 280, '2024-05-03'),
('Travel', 1300, '2024-05-09'),
('Shopping', 920, '2024-05-14'),
('Bills', 1700, '2024-05-21'),
('Entertainment', 650, '2024-05-27'),

('Food', 320, '2024-06-04'),
('Travel', 1150, '2024-06-11'),
('Shopping', 780, '2024-06-16'),
('Bills', 1600, '2024-06-22'),
('Others', 500, '2024-06-29');

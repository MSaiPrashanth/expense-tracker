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


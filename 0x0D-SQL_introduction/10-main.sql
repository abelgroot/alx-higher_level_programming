-- Create database
DROP DATABASE IF EXISTS hbtn_test_db_11;
CREATE DATABASE IF NOT EXISTS hbtn_test_db_11;
USE hbtn_test_db_11;

-- Create table
CREATE TABLE IF NOT EXISTS second_table (
	    id INT,
			    name VARCHAR(256),
					    score INT
							);

							-- Create records
							INSERT INTO second_table (id, name, score) VALUES (1, "A", 12);
							INSERT INTO second_table (id, name, score) VALUES (2, "B", 2);
							INSERT INTO second_table (id, name, score) VALUES (3, "C", -12);
							INSERT INTO second_table (id, name, score) VALUES (4, "D", 89);
							INSERT INTO second_table (id, name, score) VALUES (5, "E", 0);
							INSERT INTO second_table (id, name, score) VALUES (6, "F", 23);
							INSERT INTO second_table (id, name, score) VALUES (7, "G", 5);
							INSERT INTO second_table (id, name, score) VALUES (8, "H", 6);
							INSERT INTO second_table (id, name, score) VALUES (9, "I", -9);
							INSERT INTO second_table (id, name, score) VALUES (10, "J", 3);

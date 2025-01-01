-- Drop the database if it exists
DROP DATABASE IF EXISTS hbtn_0c_0;

-- Create the database with the correct character set and collation
CREATE DATABASE IF NOT EXISTS hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the database
USE hbtn_0c_0;

-- Create the table with default database character set and collation
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Convert the table to use the database's character set and collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Ensure the `name` column only specifies collation
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

-- Display the table structure
SHOW CREATE TABLE first_table;

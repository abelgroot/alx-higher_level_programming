-- Drop the database if it exists
DROP DATABASE IF EXISTS hbtn_0c_0;

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Use the database
USE hbtn_0c_0;

-- Create the table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Convert the database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the `name` column to ensure only the collation is applied
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

-- Display the description of the table
SHOW CREATE TABLE first_table;

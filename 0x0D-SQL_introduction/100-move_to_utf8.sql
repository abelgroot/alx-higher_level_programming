-- Script to convert hbtn_0c_0 database, first_table table, and name field to utf8mb4
USE hbtn_0c_0;

-- 1. Change the character set and collation of the database hbtn_0c_0
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- 2. Change the character set and collation of the table first_table
ALTER TABLE first_table

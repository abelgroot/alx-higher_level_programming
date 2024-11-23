-- Script to convert hbtn_0c_0 database, first_table table, and name field to utf8mb4

-- Step 1: Change the character set and collation of the entire database
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Step 2: Change the character set and collation of the first_table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 3: Change the collation of the 'name' field in first_table to utf8mb4_unicode_ci
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

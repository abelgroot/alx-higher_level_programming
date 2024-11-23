-- Script to print the full description of the table first_table
SELECT TABLE_NAME, CREATE_TABLE 
FROM information_schema.tables
WHERE table_schema = DATABASE() 
AND table_name = 'first_table';

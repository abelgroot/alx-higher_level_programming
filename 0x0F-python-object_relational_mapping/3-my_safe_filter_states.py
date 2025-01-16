#!/usr/bin/python3
"""
This script connects to a MySQL database and fetches all rows from the `states`
table where the `name` matches the user-provided argument, safely preventing
SQL injection.
Results are sorted by `states.id` in ascending order.
"""

import MySQLdb
import sys


def safe_filter_states(username, password, database, state_name):
    """
    Connect to the MySQL database and fetch states matching the name safely.
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object for query execution
    cursor = db.cursor()

    # Query with parameterized input to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and print results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close connections
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Ensure the script is executed with the correct number of arguments
    if len(sys.argv) != 5:
        sys.exit(1)

    # Call the function with command-line arguments
    safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

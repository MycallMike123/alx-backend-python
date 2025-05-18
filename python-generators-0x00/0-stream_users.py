#!/usr/bin/env python3
"""
0-stream_users.py - Stream rows from user_data table one by one using a generator
"""

import mysql.connector
from mysql.connector import Error


def stream_users():
    """Generator that yields one row at a time from user_data table"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpass",
            database="ALX_prodev"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error fetching data: {e}")


# This line makes stream_users accessible like a function from the module
# so that stream_users = __import__('0-stream_users') works as expected.
# and stream_users() calls the actual function
stream_users = stream_users


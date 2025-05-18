#!/usr/bin/env python3
"""
1-batch_processing.py - Stream and filter users in batches using a generator
"""

import mysql.connector
from mysql.connector import Error


def stream_users_in_batches(batch_size):
    """Yields batches of rows from the user_data table"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpass",
            database="ALX_prodev"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")

        batch = []
        for row in cursor:  # Loop over rows one by one
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []

        if batch:
            yield batch

        cursor.close()
        connection.close()

    except Error as e:
        print(f"Error fetching batches: {e}")


def batch_processing(batch_size):
    """
    Processes each batch to filter users over age 25 and prints them as dictionaries
    """
    for batch in stream_users_in_batches(batch_size):
        filtered = [
            {
                'user_id': user[0],
                'name': user[1],
                'email': user[2],
                'age': int(user[3])  # convert Decimal to int
            }
            for user in batch if float(user[3]) > 25
        ]
        for user_dict in filtered:
            print(user_dict)

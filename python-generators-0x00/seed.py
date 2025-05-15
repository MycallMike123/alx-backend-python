#!/usr/bin/env python3
"""
seed.py - Sets up MySQL database and populates it with data from user_data.cvs
"""


import csv
import uuid
import mysql.connector
from mysql.connector import Error


def connect_db():
    """ Connect to MySQL server (not to a specific DB) """
    try:
        return mysql.connector.connect(
                host="localhost",
                user="root",
                password="my_mysql_password"
             )

    except Error as e:
        print(f"Error connecting to MySQL server> {e}")
        return None


def create_database(connection):
    """ Create ALX_prodev database if it doesn't exist"""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    """ Connect to ALX_prodev database"""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="my_mysql_password",
            database="ALX_prodev"
        )
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None


def create_table(connection):
    """ Create user_data table if it does not exist"""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX(user_id)
            );
        """)
        connection.commit()
        cursor.close()
        print(f"Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, csv_file):
    """ Insert user from CSV into user_data table"""
    try:
        cursor = connection.cursor()
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                uid = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']
                cursor.execute("""
                    INSERT IGNORE INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (uid, name, email, age))
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting data: {e}")
    except FileNotFoundError:
        print(f"File {csv_file} not found.")


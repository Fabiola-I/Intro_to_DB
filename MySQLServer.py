#!/usr/bin/env python3
"""
MySQLServer.py
A Python script to create the 'alx_book_store' database in MySQL.
"""

import mysql.connector

def create_database():
    """Function to create the database safely."""
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # <-- replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        try:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()
        except NameError:
            pass


if __name__ == "__main__":
    create_database()


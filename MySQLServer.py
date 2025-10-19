#!/usr/bin/env python3
"""
MySQLServer.py
A simple Python script that creates the database 'alx_book_store'
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (update user/password if needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"   # 👈 replace with your actual MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create the database if it doesn’t already exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Ensure proper cleanup
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()


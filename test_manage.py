#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# wip - imports
import mysql.connector

# wip - def
def connect_database():
    try:
        connection = mysql.connector.connect(
            host="mysql-database-instance.cfuy4h1v6jlp.us-east-1.rds.amazonaws.com",
            user="mysql_admin",
            # Change password and database below
            password="mysql_sanderson_database",
            database="user"
        )
        # print("Successful connection.")
    except:
        print("Failed connection.")
        sys.exit()

    cursor = connection.cursor()
    return connection, cursor


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urec.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM user_info")
    result = cursor.fetchall()


    for x in result:
        print(x[0], x[1], x[2], x[3], "\n")


    main()

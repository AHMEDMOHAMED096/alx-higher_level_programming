#!/usr/bin/python3
""" Import MySQLdb and sys modules"""
import MySQLdb
import sys


def list_states(username, password, database_name, state_name):
    """Connect to the MySQL server"""
    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM states
        WHERE name = '{}'
        ORDER BY id ASC
    """.format(state_name))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    list_states(username, password, database_name, state_name)

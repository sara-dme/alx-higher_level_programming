#!/usr/bin/python3
""" script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where
name matches the argument."""

import MySQLdb
import sys

if __name__ == '__main__':
    """ get the states from the database"""
    db = MySQLbd.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(argv[4]))
    states = cur.fetchall()

    for row in state:
        print(row)

    cur.close()
    db.close()

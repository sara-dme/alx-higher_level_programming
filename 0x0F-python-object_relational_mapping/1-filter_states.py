#!/usr/bin/python3
""" script that lists all states with a name starting with N """


import MySQLdb
from sys import argv

"""Get states from database"""

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY states.id ASC")
    states = cur.fetchall()

    for row in states:
        print(row)

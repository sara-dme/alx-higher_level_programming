#!/usr/bin/python3
""" script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa """
import sys
import MySQLdb


if __name__ = "__main__":
    """ Get the cities from the database"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cusrsor()
    cur.execute("SELECT cities.name\
                 FROM cities INNER JOIN states\
                 ON cities.state_id = states.id\
                 WHERE states.name = %s\
                 ORDER BY cities.id ASC", (sys.argv[4]))
    row = cur.fetchall()

    if row is not None:
        print(", ".join([stat[1] for stat in row]))


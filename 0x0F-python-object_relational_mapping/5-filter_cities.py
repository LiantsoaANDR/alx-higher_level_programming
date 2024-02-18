#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3]
            )

    cursor = db.cursor()
    state = sys.argv[4]

    q = "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')\
         FROM cities\
         JOIN states ON cities.state_id = states.id\
         WHERE states.name = %s\
         ORDER BY cities.id ASC"
    cursor.execute(q, [state])

    data = cursor.fetchone()

    if data[0]:
        print(data[0])
    else:
        print()

    db.close()

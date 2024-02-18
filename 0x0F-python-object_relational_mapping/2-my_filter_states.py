#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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

    q = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state)
    cursor.execute(q)

    data = cursor.fetchall()

    for row in data:
        print(row)

    db.close()

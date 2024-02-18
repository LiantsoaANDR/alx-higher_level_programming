#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
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
    q = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(q, [state])

    data = cursor.fetchall()

    for row in data:
        print(row)

    db.close()

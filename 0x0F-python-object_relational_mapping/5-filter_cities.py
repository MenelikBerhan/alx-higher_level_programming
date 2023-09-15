#!/usr/bin/python3
"""A script that takes in the `name` of a state as an argument and
lists all `cities` of that state, using the database `hbtn_0e_4_usa`"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    no_rows = cur.execute("""SELECT c.name FROM cities c
                          INNER JOIN states s ON c.state_id = s.id
                          WHERE BINARY s.name=%s ORDER BY c.id""",
                          (sys.argv[4],))
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print(row[0], end='\n' if i == len(rows) - 1 else ', ')
    cur.close()
    db.close()

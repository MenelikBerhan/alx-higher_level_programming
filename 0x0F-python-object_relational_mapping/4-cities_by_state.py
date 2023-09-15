#!/usr/bin/python3
"""A script that lists all `cities` from the database `hbtn_0e_4_usa`"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    no_rows = cur.execute("""SELECT c.id, c.name, s.name FROM cities c
                          INNER JOIN states s
                          ON c.state_id = s.id ORDER BY c.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

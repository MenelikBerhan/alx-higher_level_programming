#!/usr/bin/python3
"""Module containing a script that lists all `states` with a `name`
starting with `N` (upper N) from the database `hbtn_0e_0_usa`"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    try:
        db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()
        no_rows = cur.execute("""SELECT * FROM states
                            WHERE name LIKE BINARY 'N%' ORDER BY id""")
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print("MySQL Error: %s" % str(e))
    for row in rows:
        print(row)
    cur.close()
    db.close()

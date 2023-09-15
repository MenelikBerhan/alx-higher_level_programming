#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the `states`
table of `hbtn_0e_0_usa` where `name` matches the argument. The script uses
place holder for the sql statement to be safe from MySQL injections!"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    no_rows = cur.execute("""SELECT * FROM states
                          WHERE BINARY name=%s ORDER BY id""", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

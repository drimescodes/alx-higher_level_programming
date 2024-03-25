#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa"""


def main(username, password, dbname):
    """Connect to a MySQL server and list all states in the database"""
    import MySQLdb
    port = 3306
    conn = MySQLdb.connect(
        host="localhost",
        port=port,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)


if __name__ == "__main__":
    import sys
    args = sys.argv
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]
    main(mysql_username, mysql_password, database_name)

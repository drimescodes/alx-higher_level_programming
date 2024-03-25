#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa with a name starting with N
"""


def main():
    """Connect to a MySQL server and list all states in the database"""
    import MySQLdb
    import sys

    args = sys.argv
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]
    port = 3306
    conn = MySQLdb.connect(
        host="localhost",
        port=port,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)


if __name__ == "__main__":
    main()

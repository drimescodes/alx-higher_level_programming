#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument and is safe from
MySQL injections.
"""


def main():
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8",
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()

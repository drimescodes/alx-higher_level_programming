#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all \
    `cities` of that state, using the database `hbtn_0e_4_usa`
"""


def main():
    """
    Main function for the script
    """
    import MySQLdb
    from sys import argv

    # Connect to a MySQL database
    db = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3], host="localhost", port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute(
        "SELECT cities.name FROM cities JOIN states ON cities.state_id = \
            states.id WHERE states.name = %s ORDER BY cities.id",
        (argv[4],),
    )

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    print(", ".join([row[0] for row in rows]))

    # Close the cursor and database
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

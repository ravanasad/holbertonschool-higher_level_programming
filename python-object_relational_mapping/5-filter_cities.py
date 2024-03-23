#!/usr/bin/python3
"""name of a state as an argument and
lists all cities of that state"""
import MySQLdb
import sys


def get_states():
    """name of a state as an argument and
    lists all cities of that state

        Args:
            username, password, database_name
            state_name -> argv[1], argv[2], argv[3], argv[4]
    """
    if len(sys.argv) != 5:
        return
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cursor = db.cursor()
    cursor.execute("SELECT c.name FROM cities c\
                   JOIN states s ON c.state_id = s.id\
                   WHERE s.name = '{:s}'\
                   ORDER BY c.id".format(sys.argv[4]))
    rows = cursor.fetchall()
    for i in range(len(rows)):
        if i == len(rows) - 1:
            print(rows[i][0])
        else:
            print(rows[i][0], end=", ")
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_states()

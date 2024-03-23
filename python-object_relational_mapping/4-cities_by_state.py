#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def get_states():
    """lists all cities from the database hbtn_0e_4_usa

        Args:
            username, password, database_name -> argv[1], argv[2], argv[3]
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cursor = db.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM cities c\
                   JOIN states s ON c.state_id = s.id\
                   ORDER BY c.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    get_states()

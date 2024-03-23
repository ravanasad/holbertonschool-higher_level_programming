#!/usr/bin/python3
"""displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys


def get_states():
    """displays all values in the states table
        of hbtn_0e_0_usa where name matches the argument

        Args:
            username, password, database_name,
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
    cursor.execute("SELECT * FROM states WHERE BINARY name='{:s}'\
                ORDER BY id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    get_states()

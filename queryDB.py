import sqlite3
from sqlite3 import Error
import os


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM Zealot")

    return rows


def select(conn, search):
    """
    Query all rows in the tasks table
    :param search:
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM Zealot WHERE slang=?", (search,))

    return rows


def main():
    database = os.path.join(os.curdir, "database.db")

    # create a database connection
    conn = create_connection(database)
    with conn:
        select(conn, "FPS") #FPS to be replaced with the search bar content


if __name__ == '__main__':
    main()

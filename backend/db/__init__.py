import sqlite3 as sql


def db_connection():
    con = None
    try:
        con = con = sql.connect("database.db")
    except sql.error as err:
        print(err)
    return con

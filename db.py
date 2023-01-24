import sqlite3

def setupConn(db_name):
    conn = sqlite3.connect(db_name)
    return conn
import sqlite3 as sql
def viewer():
    conn=sql.connect('phonebook.db')
    c=conn.cursor()
    c.execute("select * from phonebook")
    return c

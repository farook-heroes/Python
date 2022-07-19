import sqlite3 as sql

def deleter(id:int):
    conn=sql.connect('phonebook.db')
    c=conn.cursor()
    c.execute("delete from phonebook where id=:no",{'no':id})
    c.execute("select * from phonebook")
    conn.commit()
    

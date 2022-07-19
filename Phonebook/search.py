import sqlite3 as sql

def searchbyname(name : str):
    conn=sql.connect('phonebook.db')
    c=conn.cursor()
    c.execute('select * from phonebook where name like :first',{'first':'%'+name+'%'})
    return c
def searchbyno(no:str) :
    c.execute('select * from phonebook where phonenumber like :first',{'first':'%'+no+'%'})

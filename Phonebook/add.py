import sqlite3 as sql
def addition(name,phoneno):
    conn=sql.connect('phonebook.db')
    c=conn.cursor()
    c.execute("create table if not exists phonebook(id integer not null primary key autoincrement  ,name varchar(20),phonenumber varchar(10))")
    c.execute('insert into phonebook(name ,phonenumber) values(?,?)',(name,phoneno))
    c.execute('select * from phonebook') 
    conn.commit()        


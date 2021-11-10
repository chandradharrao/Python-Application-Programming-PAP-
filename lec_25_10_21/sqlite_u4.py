#sqlite : transactonal sql engine
'''
simple programming database only..
NOT for **client-server architecture**
only for single client and server architecture


sqlite3.connect() - connection to the database eg:foodsystem.db on the disk.

use ":memory" to ceate db in RAM

connection.cursor() - Intermediate object - cursor to execute commands on the dataabse on the existing connection

cursor.execute() - execute sql stateemnts 

connection.commit() - commit transaction : if not called,then ot wont be commited

connection.rollback() - rollback to the last successfull commit

connection.close() - close the connection

if db doesnt exist,then ceate and return it

NOTE:possible to execute commands without using cursor but using connection object itself
'''

import sqlite3
cxn = sqlite3.connect("college.db") #db in disk
cur = cxn.cursor()

cur.execute("create table if not exists student(name text,age integer)")
cur.execute("insert into student values('xyz',21)")
cur.execute("insert into student values('abc',22)")

#usage of placeholders (using '?').This will destructure the tuple values
info=('chandra',21)
cur.execute('insert into student(name,age) values (?,?)',info)

rows = cur.execute("select * from student")
for row in rows:
    print(row)
#sqlite : database storage engine which CAN be compared against PostgreSQL and MySQL
'''
Recommended for simple database programming only..
NOT for multiple **client-server architecture** like webapps but only for single local client and server architecture.


sqlite3.connect() - connection to the database eg:foodsystem.db on the disk.
if db doesnt exist,then create and return it.

use ":memory" to ceate db in RAM with unique id

connection.cursor() - Intermediate object - cursor to execute commands on the databse on the existing connection

cursor.execute() - execute sql stateemnts 

connection.commit() - commit transaction : if not called,then it wont be commited

connection.rollback() - rollback to the last successfull commit

connection.close() - close the connection

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
print(rows)
for row in rows:
    print(row)
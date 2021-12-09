import sqlite3

cxn = sqlite3.connect("student.db")
cursor = cxn.cursor()

cursor.execute("create table if not exists details(name text,age int)")
cursor.execute("create table emp(name text,id int)")

record = ('xxx',2)
cursor.execute("insert into details(name,age) values (?,?)",record)
rows = cursor.execute("select * from emp").fetchall()
for row in rows:
    print(row)
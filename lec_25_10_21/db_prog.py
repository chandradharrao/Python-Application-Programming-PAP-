import sqlite3

cur = sqlite3.connect("college.db").cursor()
cur.execute("create table if not exists employees(phone text,name text,age integer,marks integer)")
cur.execute("insert into employees values('9738wdewed','chandra',21,9)")
rows = cur.execute("select * from employees")
for row in rows:
    print(row)


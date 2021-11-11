'''
cur.fetchall() - fetch all rows of a query result - returns it as list of tuples - [(),(),()...] => empty list if there is no record to fetch - []

cur.fetchmany(_size) => fetch the req number of rows as a list if tuples.
_size default  = 1

cur.ftchone() - fetches single record
'''

import sqlite3
cur = sqlite3.connect("example1.db").cursor()

#works with connection and cursor object also
cur.execute("create table if not exists supplier (id integer primary key, name text not null,part_id int not null,foreign key(part_id) references parts(id))") #foreign key constraint makes part_id foreign key refering to id in parts table
cur.execute("create table if not exists parts(id integer primary key,name text not null)")

#if we try to insert record with same primary key we get integrity constraint
cur.execute("insert into parts values(1,'screw_driver'),(2,'nuts_bolts'),(3,'hammer')")
rows = cur.execute("select * from parts")
print(rows.fetchmany(1)) #**list of tuples**
# print(rows.fetchall())
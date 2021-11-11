'''
if we pass file name as ':memory:',then the db is created purely in memory and not a db file on disk.The disk file is not opened but a db is created in memory.It will cease to exists as soon as db connect is closed.They are uniquely distinguished even though they are given same fil name using IDs.
'''

import sqlite3
cor=sqlite3.connect(":memory:").cursor()

cor.execute("create table people(fname text,age int)")

#q mark style - uestion mark style
who='dhoni'
age=39
cor.execute("insert into people values(?,?)",(who,age))

#named style - key value pair
who='dhoni'
age=39
print(cor.execute('select * from people where fname=:who and age=:age',{'who':who,'age':age}).fetchone())

# print(cor.fetchone()) #fetch only after select statment
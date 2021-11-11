'''
sqlalchemy vs sqllite3 
-python lib that provides an ORM
-ORM : object relational mapping is  technique for storing,retrive,deleting and updating relational database from an object oriented program like a python program
It uses a data layer to manage transation between object orientation and relational.
-sqlalchemy uses ORM which is a translator between sqlite3 and python allowing us to use object orinted approaches in the database engine.
-maps classes(non scaler types) as table
-popular sql toolkit,written in python and an ORM

engine class - create engine object - connect with the db - connect pool and dialect together
'''

from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String

engine = create_engine('sqlite:///college.db',echo=True) #sqlite database is created,echo=should display results on cmd?

meta = MetaData() #collection of table objects and their schema construct

student_table = Table(
    'student',meta, #table name
    Column('id',Integer,primary_key=True), #create a col
    Column('name',String),
    Column('lastname',String)
) #create table like an object

meta.create_all(engine)
connection = engine.connect()

def record_creator(id,name,lastname):
    return {'id':id,'name':name,'lastname':lastname}

#insert commands as OOPs
# connection.execute(student_table.insert(),[
#     # {'id':1,'name':'chandra','lastname':'rao'},
#     record_creator(2,'shane','watson'),
#     record_creator(3,'ajinkya','rahane'),
# ])

#select command
stmt = student_table.select()
rows = connection.execute(stmt)
for row in rows:
    print(row)

#rows id>2
stmnt = student_table.select().where(student_table.c.id > 2) #c->column
rows = connection.execute(stmnt)
for row in rows:
    print(row)

#update watson to warne 
stmnt = student_table.update().where(student_table.c.lastname=='watson').values(lastname="warne")
connection.execute(stmnt)

rows = connection.execute(student_table.select())
for row in rows:
    print(row)

#delete chandra entry
stmnt = student_table.delete().where(student_table.c.name=="shane")
connection.execute(stmnt)

rows = connection.execute(student_table.select())
for i in rows:
    print(i)

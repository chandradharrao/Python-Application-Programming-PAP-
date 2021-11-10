import sqlite3

con=sqlite3.connect("college.db")
cur = con.cursor()

#commit
cur.execute("create table if not exists market(id int primary key not null, name text not null,address integer not null)")
# cur.execute(
#     "insert into market values(1,'chandra',560022) "
# )
con.commit()
print("Successfully commited")

#update adddress of record with id=1
cur.execute("update market set address=560031 where id=1")
con.commit()
print("successfully commit")

print(cur.execute("select * from market").fetchone()) #return a tuple like row=(1,'chandra',560022).Hence we could access values like row[0],row[1],row[2]
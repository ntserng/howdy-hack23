import sqlite3
from location import Location

conn = sqlite3.connect('backend/location.db')

c = conn.cursor()

## CREATE A TABLE
# c.execute("""CREATE TABLE location (
#         name text,
#         rating integer,
#         description text
#         )""")

## ADD DATA
# c.execute("INSERT INTO location VALUES (4.6, 'actually a human')")

## ADD VARIABLE DATA
location_1 = Location(4.6, 'h')
# c.execute("INSERT INTO location VALUES (:rating, :description)",
#           {'rating': location_1.rating,
#            'description': location_1.description})

## SELECT DATA
# c.execute("SELECT * FROM location WHERE rating=4.6")
# print(c.fetchall())

# c.execute("SELECT * FROM location WHERE rating=:rating", {'rating': location_1.rating})
# print(c.fetchall())

def add_post(location_1):
    with conn:
        c.execute("SELECT * FROM location WHERE rating=:rating", {'rating': location_1.rating})
        print(c.fetchall())

print(c.execute("SELECT * FROM location").fetchall())

conn.commit()

conn.close()

# sql.py - create and populate sqlite3 table

import sqlite3

# create the connection object
with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()

    # create the table
    c.execute("""create table posts(title TEXT, post TEXT)""")

    # insert dummy data into the table

    c.execute('insert into post values("Good", "I\'m good.")')
    c.execute('insert into post values("Well", "I\'m well.")')
    c.execute('insert into post values("Excellent", "I\'m excellent.")')
    c.execute('insert into post values("Okay", "I\'m okay.")')

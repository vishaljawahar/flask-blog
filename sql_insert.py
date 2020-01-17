# sql.py - create and populate sqlite3 table

import sqlite3

# create the connection object
with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()

    # insert dummy data into the table

    c.execute('insert into posts values("Good", "I\'m good.")')
    c.execute('insert into posts values("Well", "I\'m well.")')
    c.execute('insert into posts values("Excellent", "I\'m excellent.")')
    c.execute('insert into posts values("Okay", "I\'m okay.")')

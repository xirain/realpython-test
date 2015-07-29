# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("SELECT firstname, lastname from employees")
    rows = c.fetchall()
    for row in rows:
        print row[0], row[1]
# assignment3a.py
# generate 100 random numbers

import sqlite3
from random import randint

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS numbers (num INT)")
    c.execute("DELETE FROM numbers")
    nums = []
    for i in range(0,100):
        num = randint(0,100)
        nums.append(tuple([num]))

    c.executemany("INSERT INTO numbers VALUES(?)",nums)

    c.execute("SELECT * FROM numbers")

    rows = c.fetchall()

    for i in rows:
        print i[0]
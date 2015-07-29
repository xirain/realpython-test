# assignment3b.py

import sqlite3
import sys

sql = {"average":"SELECT AVG(num) FROM numbers",
    "maximum":"SELECT MAX(num) FROM numbers",
    "minimum":"SELECT MIN(num) FROM numbers",
    "sum":"SELECT SUM(num) FROM numbers"
    }
    
while True:    
    try:
        your_input = raw_input("Choices:\n1:do average\n2:do max\n3:do min\n4:do sum\nother:exit\nPlease input your select:")
        choice = int(your_input)
        if choice not in range(1,5):
            sys.exit()
        with sqlite3.connect("newnum.db") as connection:
            c = connection.cursor()
            # print sql.values()[choice-1]
            c.execute(sql.values()[choice-1])
            result = c.fetchone()

            print sql.keys()[choice-1], result[0]
    except Exception, e:
        print e
        sys.exit()
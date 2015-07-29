# assignment3b.py

import sqlite3
import sys

sql = {"average":"SELECT AVG(num) FROM numbers",
    "maximum":"SELECT MAX(num) FROM numbers",
    "minimum":"SELECT MIN(num) FROM numbers",
    "sum":"SELECT SUM(num) FROM numbers"
    }

prompt="""
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""
while True:    
    try:
        your_input = raw_input(prompt)
        if int(your_input) not in range(1,5):
            sys.exit()
        operation = {"1": "avg", "2":"max", "3":"min","4":"sum"}[your_input]
        with sqlite3.connect("newnum.db") as connection:
            c = connection.cursor()
            # print sql.values()[choice-1]
            c.execute("SELECT {}(num) FROM numbers".format(operation))
            result = c.fetchone()

            print operation + ": %f" % result[0]
    except Exception, e:
        print e
        sys.exit()
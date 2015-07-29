# hw_sql_3.py
# homework sql function

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT DISTINCT inventory.make as make, inventory.model as model, inventory.quantity as quantity, count(*) as count FROM inventory INNER JOIN orders WHERE inventory.Make = orders.make and inventory.Model = orders.model GROUP BY make,model")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
        print r[2]
        print r[3]

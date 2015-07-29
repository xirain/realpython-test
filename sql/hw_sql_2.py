# Join

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("DROP TABLE IF EXISTS orders")
    c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

    orders = [('Fords', 'A', '2012-01-01'),
    ('Fords', 'B', '2013-06-06'),
    ('Fords', 'C', '2014-07-07'),
    ('Hondas', 'AAA', '2015-07-07'),
    ('Hondas', 'ABA', '2015-09-09'),
    ('Fords', 'A', '2012-11-01'),
    ('Fords', 'B', '2013-08-06'),
    ('Fords', 'C', '2014-09-07'),
    ('Hondas', 'AAA', '2015-10-07'),
    ('Hondas', 'ABA', '2015-11-09'),
    ('Fords', 'A', '2013-01-01'),
    ('Fords', 'B', '2014-06-06'),
    ('Fords', 'C', '2015-07-07'),
    ('Hondas', 'AAA', '2015-07-27'),
    ('Hondas', 'ABA', '2015-12-09')
    ]

    c.executemany("INSERT INTO orders VALUES(?,?,?)",orders)


    c.execute("SELECT inventory.Make,inventory.Model,inventory.Quantity, orders.order_date FROM inventory INNER JOIN orders WHERE inventory.Make = orders.make and inventory.Model = inventory.model")

    rows = c.fetchall()

    for r in rows:
        print r[0],r[1]
        print r[2]
        print r[3]

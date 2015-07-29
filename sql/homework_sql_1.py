# Insert update and select
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [('Fords', 'A', 130000),
    ('Fords', 'B', 10000),
    ('Fords', 'C', 1300000),
    ('Hondas', 'AAA', 130000),
    ('Hondas', 'ABA', 30000)

    ]
    c.execute("DELETE FROM inventory")
    c.executemany("INSERT INTO inventory VALUES(?,?,?)", cars)

    c.execute("UPDATE inventory SET quantity = 65000 WHERE Make = 'Fords' and Model = 'A' ")
    c.execute("UPDATE inventory SET quantity = 15000 WHERE Make = 'Hondas' and Model = 'AAA' ")

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()

    for row in rows:
        print row[0], row[1], row[2]


    print "\nFord Cars:\n"
    c.execute("SELECT * FROM inventory WHERE Make = 'Fords'")

    rows = c.fetchall()

    for row in rows:
        # if row[0] == 'Make':
        print row[0], row[1], row[2]
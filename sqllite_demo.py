import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

curs = conn.cursor()

# curs.execute(""" CREATE TABLE employees (
#     first text,
#     last text,
#     pay integer
#     )""")

# curs.execute("INSERT INTO employees VALUES('Xavier', 'Yudd', 50000)")

curs.execute("SELECT * from employees")

print(curs.fetchone())

conn.commit()
conn.close()

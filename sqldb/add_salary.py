#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
Update ALL records within the table by increasing salary by 100k."""

# standard library
import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

# Try adding 100k to ALL rows
conn.execute("UPDATE COMPANY SET SALARY = SALARY + 100000.00")
conn.commit()

print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")

# always close your connection
conn.close()


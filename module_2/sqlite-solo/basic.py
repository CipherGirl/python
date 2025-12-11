import sqlite3
from employee import Employee


conn = sqlite3.connect('employee.db')

c = conn.cursor()

#========= CREATING TABLE =========#
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
          )""")

emp_1 = Employee('John', 'Doe', 20000)
emp_2 = Employee('Jane', 'Doe', 30000)

print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)

#========= INSERTING DATA =========#

# c.execute("INSERT INTO employees VALUES ('Mow', 'Hena', 20000)")

# BAD PRACTICE - SQL INJECTION VULNERABILITY
# c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))

# GOOD PRACTICE - USING PLACEHOLDERS
c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

# Another GOOD PRACTICE - USING DICTIONARY
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

# conn.commit()

#========= QUERYING DATA =========#
# c.execute("SELECT * FROM employees WHERE last='Doe'")

# c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
c.execute("SELECT * FROM employees WHERE last=:last", ({'last': 'Doe'}))


# print(c.fetchone())
print(c.fetchall())

conn.commit()

conn.close()
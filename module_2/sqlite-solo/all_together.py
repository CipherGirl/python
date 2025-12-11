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

# "with conn" Context manager ensures the transaction is committed
def insert_employee(emp):
    with conn: 
        c.execute("INSERT INTO employees (first, last, pay) VALUES (:first, :last, :pay)", ({'first': emp.first, 'last': emp.last, 'pay': emp.pay}))

def get_employees_by_lastname(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_employee_pay(emp, new_pay):
    with conn:
        c.execute("UPDATE employees SET pay=:pay WHERE first=:first AND last=:last", {'pay': new_pay, 'first': emp.first, 'last': emp.last})

def remove_employee(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first=:first AND last=:last", {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 20000)
emp_2 = Employee('Jane', 'Doe', 30000)


insert_employee(emp_1)
insert_employee(emp_2)

all_does = get_employees_by_lastname('Doe')

print(all_does)

conn.close()
import mysql.connector

#connecting to mysql

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@nastaciA1995",
    database="hr_database"
)

cursor = conn.cursor()

#table creation

def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            department VARCHAR(255),
            role VARCHAR(255),
            salary DECIMAL(10, 2)
        )
        """)


        #Inserting data

def add_employee(name, department, role, salary):
    cursor.execute("""
    INSERT INTO employees (name, department, role, salary)
    VALUES (%s, %s, %s, %s)            
    """, (name, department, role, salary))
    conn.commit()

#Querying data

def get_employee():
    cursor.execute("SELECT * FROM employees")
    return cursor.fetchall()


#udpating data
def update_salary(employee_id, new_salary):
    cursor.execute("""
    UPDATE employees
    SET salary = %s
    WHERE id = %s
    """, (new_salary, employee_id))
    conn.commit()

#delete data
def delete_employee(employee_id):
    cursor.execute("""
    DELETE FROM employees
    WHERE id = %s
    """, (employee_id))
    conn.commit()


if __name__ == "__main__":
    create_tables()
    add_employee("Themba Lukhele", "IT", "Software Engineer", 35000.00)
    add_employee("Anastacia Mokwena", "Marketing", "Sales Agent", 10000.00)
    print("Employees:")
    for employee in get_employee():
        print(employee)

    #update salary for employee 1
    update_salary(1, 40000.50)

    #delete employee 2
    delete_employee(2)

    print("\nAfter updates:")
    for employee in get_employee():
        print(employee)

#close connection
cursor.close()
conn.close()
class employee:
    age = 20
    salary = 120000

a = employee()
a.name = "Husnain"
print(a.name, a.age, a.salary)

b = employee()
b.name = "Ali"
print(b.name, b.age, b.salary)

class Employee:
    company = "Google" # Specific to Each Class
harry = Employee() # Object Instantiation
harry.company
Employee.company = "YouTube" # Changing Class Attribute
print(harry.company)



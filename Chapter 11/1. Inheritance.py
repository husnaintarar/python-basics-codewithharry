class Employee:
    company = "ITC"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"The name of employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC lmd"
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    def showlanguage(self):
        print(f"The name of employee is {self.name} and the language he is good at is  {self.language}")

a = Employee("Ali", 300000)
b = Programmer("Ali", 300000, "Python")

print(a.company)
print(b.company)

a.show()
b.showlanguage()
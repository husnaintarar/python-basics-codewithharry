class Employee:
    name = "Ali"
    salary = 500000
    company = "ITC"
    def show(self):
        print(f"The name of employee is {self.name} and the salary is {self.salary}")

class coder:
    language = "Python"
    def printlanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")        

class Programmer(Employee, coder):
    company = "ITC lmd"
    def showlanguage(self):
        print(f"The name of company is {self.company} and the language is  {self.language}")

a = Employee()
b = Programmer()

b.show()
b.printlanguage()
b.showlanguage()
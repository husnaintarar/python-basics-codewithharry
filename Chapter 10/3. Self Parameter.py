class Employee:
    language = "python"
    age = 20 # Class attribute
    salary = 120000

    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}. ")

    @staticmethod
    def greet(): # Now at the class level
        print("Hello, welcome to the company!")

a = Employee()
a.name = "Husnain" # Instance attribute
a.getinfo()
a.greet()
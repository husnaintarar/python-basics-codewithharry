class Employee:
    def __init__(self, name, language="python", age=20, salary=120000):
        self.name = name          # Instance attribute
        self.language = language  # Instance attribute
        self.age = age            # Instance attribute
        self.salary = salary      # Instance attribute

    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

# The constructor is called automatically here
a = Employee("Husnain") 
a.getinfo()
a.greet()
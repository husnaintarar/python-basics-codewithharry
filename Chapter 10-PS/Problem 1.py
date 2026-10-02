class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary): 
        self.name = name
        self.salary = salary

p1 = Programmer("Husnain", 120000)
print(p1.name)
print(p1.salary)
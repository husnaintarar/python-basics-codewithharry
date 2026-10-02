class Employee:
    a = 2
    def show(self):
        print(f"The class attribute of 'a' is {self.a}" )

e = Employee()
e.a = 44

e.show() # shows instant attribute

class Job:
    b = 3 
    @classmethod
    def shownum(cls):
        print(f"The class attribute of 'a' is {cls.b}" )

j = Job()
j.b = 33

j.shownum() #shows class attribute
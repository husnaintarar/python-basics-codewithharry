class Employee:
    b = 3 
    @classmethod
    def shownum(cls):
        print(f"The class attribute of 'a' is {cls.b}" )

    @property
    def name(self):
        return f"{self.fname}, {self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
       

e = Employee()
e.b = 33

e.name = "Ali Khan"
print(e.fname, e.lname)

e.shownum() 
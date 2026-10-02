#2. Create a class ‘Petsʼ from a class ‘Animalsʼ and further create a class ‘Dogʼ from ‘Petsʼ.
#   Add a method ‘barkʼ to class ‘Dogʼ.

class Animals:
    pass

class Pets:
    pass

class Dogs:
    @staticmethod
    def bark():
        print("Bark bark")

d = Dogs
d.bark()        
    
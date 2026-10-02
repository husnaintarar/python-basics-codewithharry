class MyClass:
    a = 10  # Class attribute

obj = MyClass()
obj.a = 0   # Creates a new instance attribute

print(MyClass.a)  # Output: 10
print(obj.a)      # Output: 0
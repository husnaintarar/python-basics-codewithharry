age = int(input("Enter your age: "))
if age < 5:
    raise ValueError("Age cannot be below 5")
print(age)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
Division = a/b

if(b == 0):
    raise ZeroDivisionError("b cannot be a zero")
else:
    print(f"The result of division is: {Division}")
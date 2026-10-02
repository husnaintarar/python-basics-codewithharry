x = 10
def change():
    global x #Global variable x is used to change the value of x in the global scope
    x = 20

print("Before change:", x) # Output: Before change: 10
change()
print("After change:", x) # Output: After change: 20
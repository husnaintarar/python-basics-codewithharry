print("Break Statements")
for i in range(0, 80):
    print(i)     # This will now print 0, 1, 2, and 3
    
    # This check happens on every single loop iteration
    if i == 3:
        break    # This breaks out of the loop immediately!

print("Continue Statements")
for i in range(5):
    if i == 3:
        continue    # This skips the rest of the code below it and goes to the next iteration
    print(i)     # This will now print 0, 1, 2, and 4

    
print("Pass Statements")
a = [1,2,3,4,5]
for item in a:
    pass #without pass, the program will throw an error
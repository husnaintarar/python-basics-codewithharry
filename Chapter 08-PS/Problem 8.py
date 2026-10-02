def multiply(n):
    if n == 0:
        return 1
    else:
        return n * multiply(n-1)
    
num = int(input("Enter a number: "))
result = multiply(num)
print(f"The factorial of {num} is {result}.")    
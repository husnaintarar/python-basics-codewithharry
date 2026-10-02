num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def greatest(n1, n2, n3): 
    # Use >= to handle identical numbers correctly
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

result = greatest(num1, num2, num3)

print(f"The greatest of {num1}, {num2}, and {num3} is {result}.")      


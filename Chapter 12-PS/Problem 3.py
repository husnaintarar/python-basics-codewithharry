# Write a list comprehension to print a list which contains the multiplication table of a user
# entered number

n = int(input("Enter a number: "))
multiplication_table = [f"{n} x {i} = {n * i}" for i in range(1, 11)]
print(f"Multiplication table of {n}: {multiplication_table}")
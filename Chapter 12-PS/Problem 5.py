# Store the multiplication tables generated in problem 3 in a file named Tables.txt .
n = int(input("Enter a number: "))
multiplication_table = [f"{n} x {i} = {n * i}" for i in range(1, 11)]

with open("Tables.txt", "w") as file:
    for line in multiplication_table:
        file.write(line + "\n")

print(f"Multiplication table of {n} has been written to Tables.txt")

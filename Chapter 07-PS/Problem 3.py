num = int(input("Enter a number to print its multiplication table: "))

print(f"\nMultiplication Table for {num}:")

i = 1

while i <= 10:
    result = num * i
    print(f"{num} x {i} = {result}")

    i = i + 1
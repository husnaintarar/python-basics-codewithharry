# 1. Ask the user for the number they want a table for
# Remember to wrap input() in int() to convert the text to a number!
num = int(input("Enter a number to print its multiplication table: "))

print(f"\nMultiplication Table for {num}:")

# 2. Use a for loop to iterate from 1 to 10
# Note: range(1, 11) starts at 1 and stops right before 11 (at 10)
for i in range(1, 11):
    # Calculate the result
    result = num * i
    
    # 3. Print the line using an f-string to make it look clean
    print(f"{num} x {i} = {result}")
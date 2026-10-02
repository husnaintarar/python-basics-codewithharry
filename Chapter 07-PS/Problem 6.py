# 1. Ask the user for the input number
num = int(input("Enter a number to find its factorial: "))

# 2. Initialize the factorial variable to 1
# (We start at 1 because multiplying by 0 would ruin the math!)
factorial = 1

# 3. Handle negative numbers, 0, and positive numbers
if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # Use a for loop to multiply numbers from 1 up to num
    # range(1, num + 1) stops exactly at num
    for i in range(1, num + 1):
        factorial = factorial * i

    # 4. Display the result
    print(f"The factorial of {num} is: {factorial}")
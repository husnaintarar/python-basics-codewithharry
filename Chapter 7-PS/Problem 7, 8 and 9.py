print(f"Problem 7")
n = 3

for i in range(1, n + 1):
    # Calculate the number of stars for the current row
    stars = 2 * i - 1
    print("*" * stars)
    
print(f"Problem 8")

n = 3

for i in range(1, n + 1):
    # The number of stars matches the current row number
    print("*" * i)


print(f"Problem 9")

n = 3

# Row 1: Top row (3 stars)
print("* " * n)

# Row 2: Middle row (1 space, then 2 stars)
print(" " + "* " * (n - 1))

# Row 3: Bottom row (3 stars)
print("* " * n)
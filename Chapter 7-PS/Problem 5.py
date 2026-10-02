n = int(input("Enter the value of n: "))

total_sum = 0

for i in range(1, n + 1):
    total_sum += i
print(f"The sum of first {n} natural numbers is: {total_sum}")
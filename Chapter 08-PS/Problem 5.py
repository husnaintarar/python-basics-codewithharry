def pattern(n):
    if(n == 0):
        return
    pattern(n-1)
    print("*" * n)

print("Enter the number of rows for the pattern: ", end="")
n = int(input())
pattern(n)
print("The pattern has been printed successfully.")


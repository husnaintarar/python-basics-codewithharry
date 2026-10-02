#sum of first n natural numbers using recursion
#for example if n=5 then sum=1+2+3+4+5=15
#formula for sum of first n natural numbers is n + sum(n-1)

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
    
num = int(input("Enter a number: "))
result = sum(num)
print(f"The sum of numbers from 1 to {num} is {result}.")

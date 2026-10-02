# Write a program to filter a list of numbers which are divisible by 5.
l = [10, 20, 33, 46, 55]
result = list(filter(lambda x: x % 5 == 0, l))
print(result)
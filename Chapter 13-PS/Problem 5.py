# Write a program to find the maximum of the numbers in a list using the reduce function.
l = [10, 20, 33, 46, 55]
from functools import reduce
max_num = reduce(lambda x, y: x if x > y else y, l)
print(max_num)
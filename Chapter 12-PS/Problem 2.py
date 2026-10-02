# Write a program to print third, fifth and seventh element from a list using enumerate
# function
list1 = ["Harry", "Rohan", "Shubham", "Sachin", "Rahul", "Suresh", "Ramesh"]
for i, item in enumerate(list1):
    if i in [2, 4, 6]:  # Check if the index is 2 (third), 4 (fifth), or 6 (seventh)
        print(item)
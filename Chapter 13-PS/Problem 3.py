#A list contains the multiplication table of 7. Write a program to convert it to vertical string
#of same numbers
Table = [7*i for i in range(1, 11)]
vertical_string = "\n".join(str(num) for num in Table)
print(vertical_string)
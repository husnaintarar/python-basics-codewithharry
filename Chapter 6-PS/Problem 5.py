a = ["Alice", "Bob", "Charlie", "David" ]
b = input("Enter a name to check if it is in the list: ")
if b in a:
    print(f"{b} is in the list.")   
else:
    print(f"{b} is not in the list.")
# Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not
# present, a message without exiting the program must be printed prompting the same.

for filesnames in ["1.txt", "2.txt", "3.txt"]:
    try:
        with open(filesnames) as f:
            print(f"{filesnames} is present")
    except FileNotFoundError:
        print(f"{filesnames} is not present")        
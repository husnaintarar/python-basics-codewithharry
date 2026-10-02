#Q9 — Compare two files for identical content
file_name_1 = "this.txt"
file_name_2 = "this_copy.txt"

try:
    with open("this.txt") as f1, open("this_copy.txt") as f2:
        if(f1.read() == f2.read()):
            print(f"{file_name_1} is identical to {file_name_2}.")
        else:
            (f"{file_name_1} is not identical to {file_name_2}.")

except FileNotFoundError:
    print(f"{file_name_1} or {file_name_2} does not exist.")

#Q8 — Copy this.txt
file_name = "this.txt"

try:
    with open(file_name, "r") as src, open("this_copy.txt", "w") as dst:
        dst.write(src.read()) # Indented correctly

except FileNotFoundError: # Specifically catching the missing file error
    print(f"The file '{file_name}' does not exist.")

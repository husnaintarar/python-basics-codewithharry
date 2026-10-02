#Q7 — Line number(s) where 'python' appears
file_name = "log.txt"

try:
    with open(file_name, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if "python" in line.lower():
                print(f"The word 'python' exists on line {line_number}.")
                break
        else:
            print("The word 'python' does not exist in the file.")

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
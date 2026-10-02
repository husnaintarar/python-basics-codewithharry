file_name = "log.txt"

try:
    with open(file_name, "r") as file: # Use the variable here
        for line in file:
            if "python" in line.lower():
                print("The word 'python' exists in the file.")
                break # Indented inside the 'if' statement
        else:
            print("The word 'python' does not exist in the file.")

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")



file_name = "poems.txt"
target_word = "twinkle"

try:
    with open("poems.txt", "r") as file:
        content = file.read().lower()
        if target_word in content:
            print(f"The word '{target_word}' is present in the file '{file_name}'.")
        else:
            print(f"The word '{target_word}' is not present in the file '{file_name}'.")

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
import random

def game():
    random_number = random.randint(1, 100)
    # 1. Return the score so the rest of the program can use it
    return random_number

current_score = game()
print("Your score is:", current_score)

file_name = "Hi-score.txt"

try:
    with open(file_name, "r") as file:
        # 2. Use file.read() to get the text inside the file
        # .strip() removes any accidental spaces or hidden new lines
        content = file.read().strip()

        if content == "":
            hi_score = 0
        else: 
            hi_score = int(content)

except FileNotFoundError:
    hi_score = 0

# 3. This logic is moved outside the try/except block so it runs every time
if current_score > hi_score:
    # 4. Added 'f' to format the string correctly and fixed the typo
    print(f"Congratulations! You broke the high score of {hi_score}!")

    with open(file_name, "w") as file:
        file.write(str(current_score))
else:
    print(f"The current high score is still {hi_score}. Better luck next time!")
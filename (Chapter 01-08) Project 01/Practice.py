import random

print("Welcome to the Snake Water Gun Game!")
print("Rules: ")    
print("1. Snake drinks water, water drowns gun, gun kills snake.")
print("2. You will be playing against the computer.")

names = {'s': "Snake", 'w': "Water", 'g': "Gun"}

while True:
    user_input = input("Enter 's' for Snake, 'w' for Water, or 'g' for Gun (or 'q' to quit): ").lower()
    if user_input == 'q':
        print("Thanks for playing!")
        break
    elif user_input not in names:
        print("Invalid input. Please try again.")
        continue
    computer_input = random.choice(list(names.keys()))
    print(f"Computer chose: {names[computer_input]}")

    if user_input == computer_input:
        print("It's a tie!")    

    elif (user_input == 's' and computer_input == 'w') or \
         (user_input == 'w' and computer_input == 'g') or \
         (user_input == 'g' and computer_input == 's'):
         print("You win!")          
    else:
        print("Computer wins!")
    
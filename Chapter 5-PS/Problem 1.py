# 1. Create the dictionary with Urdu words (keys) and English translations (values)
urdu_dictionary = {
    "shukriya": "thank you",
    "dost": "friend",
    "kitab": "book",
    "khana": "food",
    "paani": "water"
}

# 2. Ask the user for input
search_word = input("Enter the Urdu word you want to translate: ")

# 3. Clean up the user input (make it lowercase to match our dictionary keys)
search_word = search_word.lower()

# 4. Look up the word and print the result
if search_word in urdu_dictionary:
    translation = urdu_dictionary[search_word]
    print(f"The English translation of '{search_word}' is: {translation}")
else:
    print(f"Sorry, the word '{search_word}' is not in our dictionary.")
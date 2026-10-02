def remove_the_word(string, word):
    new_string = string.replace(word, "")
    return new_string

string = input("Enter a string: ")
word = input("Enter a word to remove from the string: ")
new_string = remove_the_word(string, word)
print(f"The new string after removing '{word}' is: {new_string}")

'''def remove(string, word):
    n = []
    for item in string:
        if item != word:
            n.append(item.strip(word))
    return n

string = input("Enter a string: ")
word = input("Enter a word to remove from the string: ")    
new_string = remove(string, word)
print(f"The new string after removing '{word}' is: {new_string}")


    '''
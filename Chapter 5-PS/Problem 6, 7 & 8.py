d = {}

name = input("Enter your name: ")
language = input("Enter your favorite programming language: ")
d.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite programming language: ")
d.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite programming language: ")
d.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite programming language: ")
d.update({name: language})

# if two people have the same name, the last one will overwrite the previous one in the dictionary
# if two people have the same favorite programming language, it will not affect the dictionary since the keys are unique

print(d)
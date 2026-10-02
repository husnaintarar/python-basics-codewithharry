#Q5 — Censor a list of words
word_to_censor = ["donkey", "stupid", "idiot"]
with open("donkey.txt", "r") as file:
    content = file.read().lower()
    for word in word_to_censor:
        content = content.replace(word, "#" * len(word))
        with open("donkey.txt", "w") as file: # 3. Write the updated content back
            file.write(content)

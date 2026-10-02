#Q4 — Replace "Donkey" in place
with open("donkey.txt", "r") as file:
    content = file.read().lower()
    content =content.replace("donkey", "######")
    with open("donkey.txt", "w") as file:
        file.write(content)

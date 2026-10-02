import os
os.makedirs("Tables_for_kids",exist_ok=True) #makedirs() creates a directory named "Tables_for_kids" if it doesn't already exist. The exist_ok=True parameter allows the function to not raise an error if the directory already exists.
for n in range(2, 21):
    with open(f"Tables_for_kids/Table_of_{n}.txt", "w" ) as file:
        for i in range(1, 11):
            file.write(f"{n} x {i} = {n*i}\n")

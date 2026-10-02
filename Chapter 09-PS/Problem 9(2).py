import filecmp

# Using it in practice
if filecmp.cmp("this.txt", "this_copy.txt"):
    print("Files are identical.")
else:
    print("Files are different.")
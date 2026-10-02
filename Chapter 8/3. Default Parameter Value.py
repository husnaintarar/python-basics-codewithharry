def greet(name = "stranger"):
     gr = "hello, " + name
     return gr 
# function body
b = greet() # name will be "stranger" in function body (default)
a = greet("harry") # name will be "harry" in function body (passed)
print(a)
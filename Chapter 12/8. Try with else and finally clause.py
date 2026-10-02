try:
    age = int(input("Enter your age: "))

except Exception as e:
    print(f"An error occurred: {e}")
    
else:
    # Executed if try was successful
    print(f"Your age is: {age}")

finally:
    # Executed no matter what
    print("Thank you for using the program.")
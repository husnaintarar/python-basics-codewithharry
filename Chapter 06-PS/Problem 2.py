a = int(input("Enter your marks: "))
b = int(input("Enter your marks: "))
c = int(input("Enter your marks: "))

total_percentage = (a + b + c) / 300

if(total_percentage >= 40):
    print("You have passed the exam.", total_percentage * 100, "%")
else:
    print("You have failed the exam.", total_percentage * 100, "%")
def  inches_to_cms(inches):
    cms = inches * 2.54
    return cms

inches = float(input("Enter length in inches: "))
cms = inches_to_cms(inches)
print(f"{inches} inches is equal to {cms} centimeters.")
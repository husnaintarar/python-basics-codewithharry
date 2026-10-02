def celcius_to_farenheit(celcius):
    farenheit = (celcius * 9/5) + 32
    return farenheit

celcius = float(input("Enter tempreture in celcius: "))
farenheit = celcius_to_farenheit(celcius)
print(f"{celcius} degree celcius is equal to {farenheit} degree farenheit.")
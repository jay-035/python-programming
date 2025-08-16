# Fahrenheit to Celsius
# C = (F - 32) * 5/9
# Celsius to Fahrenheit
# F = (C * 9/5) + 32
temperature = input("\nenter temperature to convert, add C for Celcius and F for Fahrenheit at the end, enter '0' to exit : ")
while temperature != "0":
    try:
        if temperature[-1].upper()=='F':
            fahrenheit = float(temperature[:-1])
            celcius = (fahrenheit - 32) * 5 / 9
            print(round(fahrenheit, 1),'F', "is", round(celcius, 1), 'C')
        elif temperature[-1].upper()=='C':
            celcius = float(temperature[:-1])
            fahrenheit = (celcius * 9/5) + 32
            print(round(celcius,1),'C', "is", round(fahrenheit,1), 'F')
        else:
            print("invalid input; add C or F at the end.")
    except Exception:
        print( "error parsing input. please try again.")
    temperature = input("enter temperature to convert, enter '0' to exit: ")
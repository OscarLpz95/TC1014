print("Oscar Ricardo López López")
tempf = int(input("What is the temperature?"))
tempc = (5*(tempf - 32)//9)
print("a temperature of",tempf ,"degrees Fahrenheit is", tempc ,"in Celsius")
if(tempc>=100):
    print("Water will boil at this temperature")
else:
    print("Water doesn't boil at this temperature")

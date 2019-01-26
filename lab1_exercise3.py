pennycount = input("How many pennies do you have? ")
pennyval = float(pennycount) * 0.01
nickelcount = input("How many nickels do you have? ")
nickelval = float(nickelcount) * 0.05
dimecount = input("How many dimes do you have? ")
dimeval = float(dimecount) * 0.1
quartercount = input("How many quarters do you have? ")
quarterval = float(quartercount) * 0.25
halfdolcount = input("How many half dollars do you have? ")
halfdolval = float(halfdolcount) * 0.5
dollarcount = input("How many one-dollar coins do you have? ")
dollarval = float(dollarcount)
print("\n")

if int(pennycount) != 1:
    print("You have",pennycount,"pennies\n")
else:
    print("You have 1 penny\n")
if int(nickelcount) != 1:
    print("You have",nickelcount,"nickels\n")
else:
    print("You have 1 nickel\n")
if int(dimecount) != 1:
    print("You have",dimecount,"dimes\n")
else:
    print("You have 1 dime\n")
if int(quartercount) != 1:
    print("You have",quartercount,"quarters\n")
else:
    print("You have 1 quarter\n")
if int(halfdolcount) != 1:
    print("You have",halfdolcount,"half dollars\n")
else:
    print("You have 1 half dollar\n")
if int(dollarcount) != 1:
    print("You have",dollarcount,"dollar coins\n")
else:
    print("You have 1 dollar coin\n")

totalval = pennyval + nickelval + dimeval + quarterval + halfdolval + dollarval
print("The value of all your coins is",totalval,"\n")

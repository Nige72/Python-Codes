#NS: Tip calculator #

print("Welcome to the tip calculator")

bill = float(input("What was the total bill?: £"))
tip = int(input("What percentage of tip would you like to give 10, 12, or 15?: "))
people = int(input("How many to split the bill?:" ))

newtip1 = float(bill)/(tip)
newtip2 = float(bill) + (newtip1)
newtip3 = float(newtip2)/ (people)
newtip4 = (round(newtip3,2))
newtip5 = str(newtip4)
print("Each person should pay :£", newtip5)
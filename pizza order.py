#NS: Build your own pizza #
print("Welcome to build your own pizza's")
print("Prices start at S:£5 / M:£10 / L:£15")
size = input("What size of pizza would you like? S, M, L:  ")
pepperoni = input("Would you like some pepperoni added? Y or N: ")
extra_cheese = input("Would you like extra cheese Y or N: ") 
bill = 0
if size == "s":
    bill = 5
    if pepperoni == "y":
     bill += 2
    if extra_cheese == "y":
     bill +=1
    print("Your total bill is:£",bill)
elif size == "m":
     bill = 10
     if pepperoni == "y":
      bill += 3
     if extra_cheese == "y":
      bill +=1
     print("Your total bill is:£",bill)
else:
    size == "l"
    bill = 15
    if pepperoni == "y":
      bill += 3
    if extra_cheese == "y":
      bill +=1
    print("Your total bill is:£",bill)

    


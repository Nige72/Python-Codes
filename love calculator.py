#NS Building a love calculator #
print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#Can't change above
var = name1 + name2
t = var.count("t")
r = var.count("r")
u = var.count("u")
e = var.count("e")
l = var.count("l")
o = var.count("o")
v = var.count("v")
e = var.count("e")
var1 = l+o+v+e+t+r+u+e
print(var1)
if var1 <= 10 or var1 >= 90:
  print(f"Your score is {var1}, you go together like coke and mentos")
elif var1 == 40  or var1 < 50:
   print(f"Your score is {var1}, you are alright together")
else:
   print(f"Your score is {var1}.")
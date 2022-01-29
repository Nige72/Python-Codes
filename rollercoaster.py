#NS: purchase a ticket if over 120cm update #
#NS: ask age and show ticket price#
#NS: ask for photo if yes add totals together#
print("Welcome to the rollercoaster!!")
height = int(input("What is your height in cm?:  "))
bill = 0 
if height >= 120:
 print("You may continue")
 age = int(input("What is your age:  "))
 if age < 7:
     print("You are on child rates of £3 ")
     bill = 3
 elif age <= 12:
     print("You are on junior rates of £5 ")
     bill = 5
 elif age <= 18:
     print("You are young adult rates of £7 ")
     bill = 7
 elif age >= 19 and age <= 44:
     print("Adult prices are £10 ")
     bill = 10
 elif age >= 45 and age <= 65:
     print("Happy mid life crisis")
     
 photo = input("Would you like a photo? y/n: ")
 if photo == "y":
        bill += 3
        print("Your bill will be:£",bill)
 else:
     print("Your bill for the ride is:£",bill)

else:    
 print("To small to ride the rollercoaster sorry about that")
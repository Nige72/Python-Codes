#ND: Checking for leap years #

year = int(input("What year do you wish to check?:"))
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0:
          print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
  print("not a leap year")







    



 


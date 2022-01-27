#NS writing a BMI converter with aditional if & elif#

height = input("Enter your height in M: ")
weight = input("Enter your weight in KG: ")
var1 =float(weight) / float(height)**2
bmi = int(var1)
if bmi <= 18.5:
    print(bmi, "You are underweight")
elif bmi <= 25:
    print(bmi, "You are a nice healthy weight")
elif bmi <= 30:
    print(bmi, "You are overweight") 
elif bmi <= 35:
    print(bmi, "You are obese")
elif bmi > 35:
    print(bmi, "You are clinically obese")

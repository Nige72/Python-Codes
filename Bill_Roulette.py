#NS: Bill roulette
import random
names_string = input("Can I have everyones name please seperated by a comma. ")
names = names_string.split(", ")
var = len(names)
var1 = random.randint(0, var -1)
person_to_pay = names[var1]
print(person_to_pay)
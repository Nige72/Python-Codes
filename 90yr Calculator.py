#NS: Death calculator for 90 yrs#
age = input("what is your current age? ")
#print(type(age))
age_as = int(age)
years = 90 - age_as
days = years * 365
weeks = years * 52
months = years * 12
#fstatement below allows all values to be printed#
print(f" Number of years {years}, number of days {days}, number of weeks {weeks}, number of months {months}")
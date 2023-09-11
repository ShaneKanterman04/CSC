#convert formula to programming statement
'''
Suppose you want to deposit a certain amount of money into
a savings account and leave it alone to draw interest for the
next 10 years. At the end of 10 years, you would like to have
$10,000 in the account. How much do you need to
deposit today to make that happen?
You can use the following formula to find out:
'''

futureValue=float(input("Enter the desired future value amount: "))
rate=float(input("Enter the rate: "))
years=int(input("Enter the number of years: "))


presentValue=futureValue / (1+rate)**years

#display
print("You will need to deposit this amount:  ", format(presentValue, '.2f'))
# In-class exercise

'''A customer in a store is purchasing five items.
Write a program that asks for the price of each item,
then displays the subtotal of the sale,
the amount of sales tax, and the total.
Assume the sales tax is 7 percent.
'''

item1=float(input("Enter cost of item 1: "))
item2=float(input("Enter cost of item 2: "))
item3=float(input("Enter cost of item 3: "))
item4=float(input("Enter cost of item 4: "))
item5=float(input("Enter cost of item 5: "))

subtotal=item5+item4+item3+item2+item1
print("Sub Total: ", subtotal)

tax=subtotal*.07
print("Sales Tax: ", format(tax,'.2f'))

total=subtotal+tax
print("Total: ", total)
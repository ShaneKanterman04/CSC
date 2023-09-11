'''Shane Kanterman HW 1'''

funds=0
shares=2000
stockPrice=40.0
commissionRate=.03

#Buy stock
totalCost=shares*stockPrice
commision=totalCost*commissionRate
funds-=(totalCost+commision)

#Print purchase info
print('Joe paid $' + format(totalCost, '.2f') +' for the stock')
print('Joe paid $' + format(commision, '.2f') + ' in commision')
print('Joe has $' + format(funds, '.2f'))

#Sell stock
stockPrice=42.75
saleValue=stockPrice*shares
commision=saleValue*commissionRate
funds+=saleValue
funds-=commision

#print sale info
print('Joe sold the stock shares for $' + format(saleValue, '.2f'))
print('Joe paid his broker $' + format(commision, '.2f'))
print('Joe made/lost $' + format(funds, '.2f'))
#This program gets three test scores and displays average
#Congradulates user if the avg is higher than 89

#get three test scores
test1=float(input("Enter the score for test 1:"))
test2=float(input("Enter the score for test 2:"))
test3=float(input("Enter the score for test 3:"))

#calculate avg test score
average=(test1+test2+test3)/3

print("Your average test score is ",format(average, '.2f'))

if average >= 90:
    print("Congradulations!!")
    print("That is a great average!")
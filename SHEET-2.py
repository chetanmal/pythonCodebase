#SHEET-2 CONDITIONAL STRUCTURE
#Q1
'''
num= int(input("Enter a number: "))

if (num%2==0):
    print(num," is Even")
else:
    print(num," is Odd")
'''
#Q2
'''
num1= int(input("Enter number 1: "))
num2= int(input("Enter number 2: "))

if num1>num2:
    print(num1," is greater than ",num2)
else:
    print(num2," is greater than ",num1)
'''
#Q3
'''
num1= int(input("Enter number 1: "))
num2= int(input("Enter number 2: "))
num3= int(input("Enter number 3: "))

if num1>num2 and num1>num3:
    print(num1," is the biggest number")
elif num2>num3:
    print(num2," is the biggest number")
else:
    print(num3," is the biggest number")
'''
#Q4
'''year= int(input("Enter a year(yyyy): "))
if((year%4==0) and ((year%400==0) or (year%100!=0))) :
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
'''
#Q5
'''
calls = int(input("Enter number of calls: "))

if calls <= 100:
    bill = 200 
elif calls > 100 and calls <= 150:
    calls = calls - 100
    bill = 200 + (0.60 * calls)
elif calls > 150 and calls <= 200:
    calls = calls - 150
    bill = 200 + (0.60 * 50) + (0.50 * calls)
else:
    calls = calls - 200
    bill = 200 + (0.60 * 50) + (0.50 * 50) + (0.40 * calls)

print("Total bill amount is", bill)
'''
#Q6
'''
sub1 = int(input("Enter marks obtained in subject 1: "))
sub2 = int(input("Enter marks obtained in subject 2: "))
sub3 = int(input("Enter marks obtained in subject 3: "))

avg_marks =(sub1+sub2+sub3)/3
print("Average mark:",avg_marks)

if avg_marks>=90:
    print("Grade is A")
elif avg_marks>=80:
    print("Grade is B")
elif avg_marks>=70:
    print("Grade is C")
elif avg_marks>=60:
    print("Grade is D")
else:
    print("Grade is F")
'''
#Q7
'''
day= int(input("Enter a number 1-7 : "))

if (day==1):
    print(day," is Sunday")
elif (day==2):
    print(day," is Monday")
elif (day==3):
    print(day," is Tuesday")
elif (day==4):
    print(day," is Wednesday")
elif (day==5):
    print(day," is Thursday")
elif (day==6):
    print(day," is Friday")
elif (day==7):
    print(day," is Saturday")
else:
    print("Wrong Input!!!!!")
'''
#Q8
'''
letter = input("Enter a letter: ")
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, "is a vowel.")
else:
    print(letter, "is a consonant.")
'''
#SOLUTION 2
'''
letter = input("Enter a letter: ")
if letter in ('a','e','i','o','u'):
    print(letter," is a vowel.")
else:
    print(letter,"is a consonant.")
'''
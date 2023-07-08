#SHEET-3 LOOPING STRUCTURE
#Q1
'''
for i in range(1,11):
    print(i)
'''
#Q2
'''
num = int(input("Enter a positive integer: "))
sum = 0
for i in range(1,num+1):
    sum+=i
print("Sum of natural numbers upto",num,"is",sum)
'''
#Q3
'''
num= int(input("Enter a positive number: "))
print("Multiplication table of",num,":-")
for i in range(1,11):
    print(num,"*",i,"=",num*i)
'''
#Q4
'''
um = int(input("Enter a positive number: "))
fact=1
i=num
while i>1:
    fact=fact*i
    i=i-1
print("Factorial of",num,"is",fact)
'''
#Q5
'''
base = int(input("Enter a number: "))
power = int(input("Enter the power it is raised to: "))
res=1
for i in range(1,power+1):
    res= res * base
print(base,"raised to power",power,"is",res)  
'''
#Q6
'''
num = int(input("Enter a positive integer: "))
temp = num
rev_no=0
while temp>0:
    digit = temp%10
    rev_no= digit + rev_no*10
    temp= int(temp/10)
print("Reverse of",num,"is",rev_no)
'''
#Q7
'''
num = int(input("Enter a positive integer: "))
temp = num
sum=0
while temp>0:
    digit = temp%10
    sum=sum+digit
    temp= int(temp/10)
print("Sum of digits of",num,"is",sum)

Output
'''
#Q8
'''
num = int(input("Enter a positive integer: "))
temp = num
rev_no=0
while temp>0:
    digit = temp%10
    rev_no= digit + rev_no*10
    temp= int(temp/10)
if num==rev_no:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")
'''
#Q9
'''
num = int(input("Enter a positive integer: "))
flag = False
for i in range(2,num):
    rem = num % i
    if rem == 0:
        flag=True
        break

if flag==True or num <=1:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")
'''
#Q10
'''
positive=negative=zero=0
choice = 'Y'
while choice=='y'or choice=='Y':
    num = int(input("Enter a number: "))
    if num==0:
        zero=zero+1
    elif num>0:
        positive=positive+1
    else:
        negative=negative+1

    choice=input("Do you wish to continue(Y,N)?: ")
	
print("Positive numbers:",positive,", Negative numbers:",negative,", Zeros:",zero)
'''
#Q11
'''
min = 99999
max = 0
choice='y'
while choice == 'y' or choice=='Y':
    num = int(input("Enter a number: "))
    if(num > max):
        max = num
    if(num < min):
        min = num
    choice = input("Do you wish to continue(Y/N)?: ")

print("Maximum number:", max, "\nMinimum number:", min)
'''
#Q12
'''
number=sum=0
for i in range(0,1000):
    number=i
    sum=0
    while number>0:
        digit = number%10
        sum=sum+pow(digit,3)
        number= int(number/10)
    if i==sum:
        print(i)
'''
#Q13
'''
n = int(input("Enter number of terms required: "))
first=third=0
second=1
print(first,second,end=' ')
for i in range(3,n+1):
    third=first+second
    print(third,end=' ')
    first=second
    second=third
'''
#Q14

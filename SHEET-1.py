#SHEET-1 VARIABLE,OPRATOR AND EXPRESSION
#Q1
'''
a=input("Enter your Name:")
print(a)
'''
#Q2
'''
a=int(input('Enter the 1st no:'))
b=int(input('Entr the 2nd no:'))
c='The total of A and B is:',a+b
print(c)
'''
#Q3
'''
c=eval(input('Enter the Celcius tempreature:'))
f=9/5*c+32
print('The tempreature in Fahrenite is:',f)
'''
#Q4
'''
P=eval(input('Enter the Principl:'))
R=eval(input('Enter the Rate:'))
T=eval(input('Enter the time:'))
SI=P*R*T/100
print('The total Simple intrest is:',SI)
'''
#Q5
'''
s=int(input('Enter seconds: '))
h=s // 3600
m=(s % 3600) // 60
s=s % 60
print('Hours:', h)
print('Minutes:', m)
print('Seconds:', s)
'''
#Q6
'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=a
a=b
b=c
print("After swapping, first number is ",a," and second number is ",b)
'''
#Q7
'''
num1=int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("After swapping, first number is ",num1," and second number is ",num2)
'''
#Q8
'''
radius= float(input("Enter radius of circle: "))
area = 3.14*radius**2
circumference = 2*3.14*radius
print("Area of circle:",area)
print("circumference of circle:",circumference)
'''
#Q9
'''
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length*width
circumference = 2*(length+width)

print("Area of rectangle: ",area)
print("Circumference of rectangle: ",circumference)
'''
#Q10
'''
principle = int(input("Enter principle amount: "))
rate = int(input("Enter interest rate: "))
time = int(input("Enter time(years): "))

ci= principle * pow((1 + rate / 100), time) - principle

print("Compound interest is ",ci)
'''
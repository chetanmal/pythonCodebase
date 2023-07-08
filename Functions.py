

#Pactice: You are  having a list,
#in the list you have some number ending with 0's,
#you have to print those numbers...!!

'''
list_1=input('Enter the values for the list:')
list_2=[int(chetan) for chetan in list_1.split(',')]
def list_keyword(a):
    for chetan in list_2:
        if chetan % 10==0:
            print(chetan)
list_keyword(list_2)
list_2=[100,200,444,333]
list_keyword(list_2)
'''

#Q1
'''
def find_max(a,b,c):

    find_digit=a

    if b>find_digit:
        find_digit=b

    if c>find_digit:
        find_digit=c
    print('The largest number is:',find_digit)

def main():
    digit_1=int(input('Enter the 1st num:'))
    digit_2=int(input('Enter the 2nd num:'))
    digit_3=int(input('Enter the 3rd num:'))

    find_max(digit_1,digit_2,digit_3)
main()
'''

#Q2

'''
def is_vowel(chetan):
    vowels='aeiouAEIOU'
    if chetan in vowels:
        return True
    else:
        return False
def main():
    total=0
    a=input('Enter your sentence:')
    for count in a:
        if is_vowel(count):
            total=total+1
    print("The total number of vowels in ",total)

main()    
'''

#Q3
'''
def is_prime(digits):
    for chetan in range(2,digits):
        if digits%chetan==0:
            return False
    return True

def main():
    for i in range(2,501):

        if is_prime(i):

            print(i,end=' ')
main()
'''
#Q4
'''
def is_function(term):
    sum=0
    for i in term:
        sum=sum+i**3
    print (sum)

def main():
    a=[]
    b=int(input('How many elements do you want:'))
    for i in range(b):
        total=int(input('Enter the numbers:'))
        a.append(total)
    is_function(a)

main()
'''
#Q5
'''
def zero_ending(score):
    sum=0
    for i in score:
        if i%10==0:
            sum=sum+i
    print(sum)

def main():
    lst=[]
    a=int(input('Enter how many do you need:'))
    for chetan in range (a):
        total=int(input('Enter your terms:'))
        lst.append(total)
        zero_ending(lst)
main()
'''
#Q6
'''
def count_now(places):
     for i in places:
        if len(i)>5:
         print(i)

def main():
    places=int(input('How many elemnts do you want:'))
    r=[]
    for place in range (places):
        a=input('Enter the names of places:')
        r.append(a)
    count_now(r)
main()
'''
#Q7
'''
def element(list):
    for digit in list:
        if digit.isdigit():
            print(digit*3)
        elif digit.isalpha():
            print(digit+"#")

def main():
    values_and_words=int(input('Enter How many variable you wanna enter:'))
    for value in range(values_and_words):
        variables=input('Enter the variables:').split(',')
        element(variables)

main()
'''
#Method_2
'''
def element(list):
    for digit in list:
        if digit.isdigit():
            print(digit*3)
        elif digit.isalpha():
            print(digit+"#")

def main():
    
    values_and_words=input('Enter the variables:').split(',')
    lst=[]
    for value in values_and_words:
        lst.append(value)
        element(lst)
   
main()
'''
#Q9
'''
def half_and_half(list):
    length=len(list)
    middle=length//2
    
    if length%2==0:
        list[:middle], list [middle:]= list[middle:],list[:middle]

    else:
       list[:middle+1], list[middle:+1]= list[middle:+1], list[:middle+1]

    return list 
    
user_input = input("Enter a list of numbers: ").split(' ')
my_list = [int(num) for num in user_input]

modified_list = half_and_half(my_list)
print("Modified list:", modified_list)
'''
#Q8
'''
def search(list,position):
    first=0
    last=len(list)-1
    while first <= last:
        middle= first+last//2

        if list[middle]==position:
            return middle
        if list[middle] < position:
            last= middle-1
        else:
            first= middle+1
        return -1

a=input('Enter the numbers for the list in descendiing order:' ).split(' ')
list=[int(chetan)for chetan in a ]
postion=int(input('Enter the number you wanna find:'))
postioning=search(list,postion)
if postioning !=-1:
    print('The value',postion,'is found at posiotn',postioning)
else:
    print('The values you enter',postion,'is not found in the list')
'''

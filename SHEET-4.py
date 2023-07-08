#SHEET-4 STRING
#Q1
'''
text = input('Enter a string: ')
vowel = 0

for ch in text:
    if ch in 'aeiouAEIOU':
        vowel += 1

print('No of vowels are', vowel)
'''
#Q2
'''
text = input('Enter a string: ')
lower = upper = digit = space = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch == ' ':
        space += 1

print('The number of uppercase letters:', upper)
print('The number of lowercase letters:', lower)
print('The number of digits:', digit)
print('The number of whitespace characters:', space)
'''
#Q3
'''
text = input('Enter a string: ')
newtext = text[-1]+text[1:-1]+text[0]
print('New string:', newtext)
Output
'''
#Q4
'''
text = input('Enter a string: ')
newtext = ''
for ch in text:
    newtext = ch + newtext
print('New string:', newtext)
'''
#SOLUTION-2
'''
text = input('Enter a string: ')
newtext = text[::-1]
print('New string:', newtext)
'''
#Q5
'''
text = input('Enter a string: ')
newtext = text[1:] + text[0]
print('New string:', newtext)
'''
#Q6
'''
text = input('Enter a string: ')
space1 = text.find(' ')
space2 = text.find(' ',space1+1)
newtext = text[0] +'. '  + text[space1+1] +'. ' + text[space2+1] +'.'
print('New string:', newtext)
'''
#Q7
'''
text = input('Enter a string: ')
length = len(text)

flag = True

for i in range(0,length//2):
    if text[i] != text[length-1-i]:
        flag = False
        break

if flag == True:
    print('String is palindrome')
else:
    print('String is not palindome')
'''
#SOLUTION-2
'''
text = input('Enter a string: ')
#reverse string
newtext = text[::-1]

if text == newtext:
    print('String is palindrome')
else:
    print('String is not palindrome')
'''
#Q8
'''
text = 'SHIFT'
for i in range(0,6):
    newtext = text[i:] + text[:i]
    print(newtext)
'''
#Q9
'''
length = lower = upper = digit = False

password = input('Enter the password: ')

if len(password)>= 8:
    length = True
    
    for letter in password:
        if letter.islower():
            lower = True
        elif letter.isupper():
            upper = True
        elif letter.isdigit():
            digit = True


if length and lower and upper and digit:
    print('That is a valid password.')
else:
    print('That password is not valid.')
'''
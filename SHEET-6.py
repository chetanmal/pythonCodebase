#SHEET=6 DICTIONARY

#Q1
'''
string_1=input('Enter your string:').lower()

string_1=string_1.split()

unique_words=set(string_1)

print(unique_words)

for i in unique_words:
    print(i)
'''

#Q2

'''
element_1=input('Enter the elements:').split()

single_occure=[]

for i in element_1:

    if element_1.count(i)==1:

        single_occure.append(i)

print(single_occure)
'''
#Q3
'''
d={}
while True:
  employee=input('Enter the name of the Employee:')

  salary=int(input('Enter the salary amount:'))

  d['Employee name:',employee]='salary:',salary

  cons=input('Do you want to add more(yes/no):')

  if cons=='no' or 'NO':
     break
  
print(d)
'''
#Q4
'''
d={'even':[],'odd':[]}

while True:
    elements=input('Enter the numbers, after done type "DONE":')
    if elements == 'done':
        break
    if elements.isdigit():
        a=int(elements)
        if a % 2 == 0:
            d['even'].append(a)
        else:
            d['odd'].append(a)
    else:
        print('Invalid input')
print(d)
'''

#Q5

d={}
sentence=input('Enter your sentence:').split()

for char in sentence:
    long=len(char)
    if long in d:
        d[long]=d[long]+1
    else:
        d[long]=1

print(d)

#Q6

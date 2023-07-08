#SHEET-5 LISTS


#Q1
'''
mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter',str(size),'elements')

for i in range(size):
    data = int(input())
    mylist.append(data)

print('Alternate elements are:')

for i in range(0,size,2):
    print(mylist[i])

'''
#Q2
'''
a=input('Enter a list of element:').split()
print('Original lsit:',a)
RL=[]
for i in range(len(a)-1,-1,-1):
    RL.append(a[i])
print(RL)
'''
#Q3
''''
L=[]
a=int(input('how many element you want for the list:'))
print('Enter',str(a),'elements(ONLY NUMBERS)')
for i in range(a):
    chetan=int(input())
    L.append(chetan)
max=0
for chetan in L:
    if chetan>max:  
        max=chetan
print('The largest of the list is',max)
'''
#Q4
'''
l=[]
a=int(input('How many element do you want?:'))
print('Enter',str(a),'Elements')
for i in range(a):
    chetan=input()
    l.append(chetan)
print(l)
b=l[a-1]
for i in range(a-1,0,-1):
    l[i]=l[i-1]
l[0]=b
print('The updated list is:',l)
'''
#Q5
'''
a=input('Enter your String:')
b=a.split()
c=input('Enter the word you want to delete:')
d=False
for chetan in b:
    if chetan==c:
        b.remove(chetan)
        d=True
if d:
    a=' '.join(b)
    print('String after deletion:',a)
else:
    print('Wrong input, PLEASE TRY AGAIN')
'''
#Q6
'''
a=input('Enter your date(mm/dd/yyyy):')
b=a.split('/')
day=int(b[1])
year=int(b[2])
month=int(b[0])
if month==1:
    print('January',day,year)
elif month==2:
    print('Fabruary',day,year)
elif month==3:
    print('March',day,year)
elif month==4:
    print('April',day,year)
elif month==5:
    print('May',day,year)
elif month==6:
    print('June',day,year)
elif month==7:
    print('July',day,year)
elif month==8:
    print('September',day,year)
elif month==9:
    print('October',day,year)
elif month==10:
    print('November',day,year)
elif month==11:
    print('January',day,year)
elif month==12:
    print('December',day,year)
'''
'''
monthsList = ["January", "Fabruary"]

monthsList[month]
'''
#Q7
'''
a=input('Enter your String:')
b=a.title()
print(b)
'''
#Q8
'''
row =int(input('No. of Row?:'))
column=int(input('No. of Columns?:'))
matrix=[]
print('type the values for the MATRIX:')

for chetan in range (row):
    parts=[]
    for i in range(column):
        parts.append(int(input()))
    matrix.append(parts)
print(matrix)

for chetan in matrix:
    for i in chetan:
        print(i,end=' ')
    print()

for chetan in matrix:
    su=0
    for i in chetan:
        su=su+i
    print('sum of row:',chetan,":-",su)
'''
#Q9
'''
row=int(input('No. of Row:'))
column=int(input('No. of Column:'))
print()
print('Enter the inputs for matrix_A:')

matrix_a=[]

for chetan in range (row):
    parts=[]
    for i in range(column):
        parts.append(int(input()))
    matrix_a.append(parts)
print(matrix_a)

print()
print('Enter the inputs for matrix_b:')

matrix_b=[]

for chetan in range (row):
    parts=[]
    for i in range(column):
        parts.append(int(input()))
    matrix_b.append(parts)

print(matrix_b)

print()

for chetan in range(row):
    matrix_c=[]
    for i in range (column):
        a=matrix_a[chetan][i]+matrix_b[chetan][i]
        matrix_c.append(a)
    print(matrix_c)
'''
#Q10
'''
row=int(input('No. of Row:'))
column=int(input('No. of Column:'))
print()
print('Enter the inputs for matrix_A:')

matrix_a=[]

for chetan in range (row):
    parts=[]
    for i in range(column):
        parts.append(int(input()))
    matrix_a.append(parts)
print(matrix_a)

print()
print('Enter the inputs for matrix_b:')

matrix_b=[]

for chetan in range (row):
    parts=[]
    for i in range(column):
        parts.append(int(input()))
    matrix_b.append(parts)

print(matrix_b)

print()

for chetan in range(row):
    matrix_c=[]
    for i in range (column):
        a=matrix_a[chetan][i]*matrix_b[chetan][i]
        matrix_c.append(a)
    print(matrix_c)     
'''











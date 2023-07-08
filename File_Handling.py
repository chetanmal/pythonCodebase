#Q1
'''
a=open("chetan.txt","r")
b=a.read()
print(b)
'''
#Q2
'''
a=open('chetan.txt','r')
b=(a.readlines())
total=0
for chetan in b:
    if chetan[0]!='t' or chetan[0]!='T':
        total=total+1
print('Total "T" in the file:',total)
'''
#Q3
'''
a=open('chetan.txt','r')
total=0
b=a.read()
alpha=b.split()
for chetan in alpha:
    total=total+1
print('The total number of word in the text file are',total)
'''
#Q4
'''
a=open('chetan.txt','r')
find=0
b=a.read()
search=b.split()
for chetan in search:
    if chetan=='the' or chetan== 'The':
        find=find+1
print('the total no. of','the','in your text file are:', find)
'''
#ask the user method
'''
a= open('chetan.txt', 'r')
count = 0
content = a.read()
words = content.split()
word_to_search = input('Enter the word to search: ')

for word in words:
    if word == word_to_search:
        count += 1

print('The total number of occurrences of the word', word_to_search, 'in the text file is:', count)

a.close()
'''
#Q5
'''
a=open('chetan.txt','r')
b=a.read()
words=b.split()
for chetan in words:
    if len(chetan)<4:
        print(chetan, end=', ')
'''
#Q6
'''
file=open('chetan.txt','r')
count=0
count_1=0
read=file.read()
words=read.split()
for chetan in words:
    if chetan== 'this':
        count=count+1
print('total word "this" avaible in your text file:',count)
for i in words:
    if i =='these':
        count_1=count_1+1
print('Total words "these" avaible in your text file:',count_1)
'''
#Q7
'''
a=open('chetan.txt','r')
total=0
b=a.read()
words=b.split()
for chetan in words:
    if chetan[-1]=='e' or chetan[-1]=='E':
        total=total+1
print(total)
'''
#asking user method
'''
a=open('chetan.txt','r')
total=0
b=a.read()
words=b.split()
enter_the_word=input('Enter the ending letter with which you wanna find the letter:')
for chetan in words:
    if chetan[-1]==enter_the_word or chetan[-1]== enter_the_word:
        total=total+1
print(total)
'''
#Q8
'''
file=open('chetan.txt','r')
words=file.read()
total=0
for letter in words:
    if letter.isupper():
        total=total+1
print('Total uppacse availble:',total)
'''
#Q9
'''
file=open("chetan.txt","r")
words=file.read()
for chetan in words:
    print(chetan, end="#")
'''
#Q10
'''
file=open('words.txt','r')
words=file.read()
modified=words.replace('J','I') or words.replace('j','i')
print('Modified sentence:',modified)
'''
#Q11
'''
def AMcount():
    file=open('chetan.txt','r')
    words=file.read()
    count=0
    count_1=0
    for letter in words:
        if letter=='A' or letter=='a':
            count=count+1
        elif letter=='M' or letter=='m':
            count_1= count_1+1

    print('Total no. of A and a:',count)
    print('Total no. of M and m:',count_1)

AMcount()
'''
#Q12
'''
import pickle
def createFile():
    while True:
        book_no = input("Enter Book Number (NOT:0): ")
        book_name = input("Enter Book Name:")
        author = input("Enter Author Name:")
        price = float(input("Enter Price:"))
        book = (int(book_no), book_name, author, price)
        file=open("Book.dat", "ab")
        pickle.dump(book, file)
        print("Record added.")
        again=input('Do you want to add more books(yes/no)?:')
        if again=='yes':
             continue
        else:
             break
def countRec(author):
    total=0
    file=open("Book.dat", "rb")
    while True:
        try:
            book=pickle.load(file)
            if book[2]==author:
                total=total+1
        except EOFError:
                break
    return total
createFile()

author_name = input("Enter the author name to count books for: ")
total=countRec(author_name)
print('Number of books by',author_name,':',total)
'''
#Q13
'''
import pickle
def count_rec():
    student_list=[]
    while True:
        admission_number = int(input("Enter admission number: "))
        name = input("Enter name: ")
        percentage = eval(input("Enter percentage: "))
        student_info = [admission_number, name, percentage]
        student_list.append(student_info)
        choice = input("Do you want to add more student information? (yes/no): ")
        if choice!="yes":
            break
    filename="STUDENT.DAT"
    try:
        file=open(filename, "wb")
        for student_info in student_list:
            pickle.dump(student_info, file)
        count = 0
        file=open(filename, "rb")
        while True:
            try:
                student_info = pickle.load(file)
                admission_number, name, percentage = student_info
                if percentage == percentage > 75 or percentage==75:
                    print("Admission Number:", admission_number)
                    print("Name:", name)
                    print("Percentage:", percentage, "\n")
                    count=count+1
            except EOFError:
                break
        print("Number of students scoring above 75%:", count)
    except FileNotFoundError:
        print("File not found.")
    
count_rec()
'''
#Q14
'''
import pickle
def employee_records():
    while True:
        empcode=int(input('Enter the Employee code:'))
        name=input('Enter the Name of the Employee:')
        salary=eval(input('Enter the Amount of salary they are getting:'))
        employee={'empcode':empcode,'name':name,'salary':salary}
        file=open('employee.dat','wb')
        pickle.dump(employee,file)
        print('RECORD ADDED ^-^')

        ask=input('Do you want to add more recodes?(yes/no:)')
        if ask!='yes':
            break
    try:
        file=open('employee.dat','wb')
        for chetan in 

    file.close()
employee_records()

def salary_recordes():
    file=open('employee.dat','rb')
    greater=0
    lower=0
    equal=0
    try:
        while True:
            display=pickle.load(file)
            if display<30000:
                greater=greater+1
                print('Salary greater than 30k:',greater)
            elif display>30000:
                lower=lower+1
                print('Salary lower than 30k',lower)
            elif display==30000:
                equal=equal+1
                print('Salary equal to 30k',equal)
    except EOFError:
        pass
    file.close()
salary_recordes()

'''
import pickle
def employee_records():
    try:
        file=open('employe.dat','rb')
        data=pickle.load(file)
    except FileNotFoundError:
        data={}

    while True:
        empcode=int(input('Enter the Employee code: '))
        name=input('Enter the Name of the Employee: ')
        salary=eval(input('Enter salalry amount of the employee: '))
        
        data[empcode]={'name':name,'salary':salary}
        file=open('employee.dat','wb')
        a=pickle.dump(data,file)
        print('RECORD ADDED ^-^')
        choose= input('Do you want to ADD more records?(yes/no):')
        if choose!='yes':
            break

    search_amount=input('Do you want to search for the salary(yes/no):')
    if search_amount=='yes':
                file=open('employee.dat','rb')
                while True:
                    try:
                        count=pickle.load(file)
                        limit_amount=int(input('Enter the limit amount:'))
                        search_type=input('what kind of search do you wanna have(greater, lower, equal):')
                        if search_type=='greater':
                            t=data['salary']>limit_amount
                            print(t,end=' ')
                        elif search_type=='lower':
                            z=count['salary']<limit_amount
                            print(z,end=' ')
                        elif search_type=='equal':
                            g=count['salary']==limit_amount
                            print(g,end=' ')
                    except EOFError:
                         pass
                    break
employee_records()
 
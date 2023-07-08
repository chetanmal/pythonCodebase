#CLASS
#Q1
'''
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimetre(self):
        print ("Perimetre=", 2*(self.length*self.breadth))
    def area(self):
        print ("Area=", self.length*self.breadth)
rectangle_lenght=int(input('Enter the NO. for the length: '))
rectangle_breath=int(input('Enter the NO. for the breath: '))
R1=rectangle(rectangle_lenght,rectangle_breath)
R1.perimetre()
R1.area()
'''
#Q2
'''
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(self.name)
        print(self.age)
name=input("Enter the name of the student: ")
age=int(input('Enter the age of the student: '))
S1=student(name,age)
S1.display_info()
'''
#Q3
'''
class bank_accound:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print('Rs',amount,' deposited :)') 
        else:
            print('Invalid deposit ammount please add positive amount :(') 
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print('Rs',amount,'withdrawn from your account :)')
        else:
            print('Insufficient Balance')
    def display_balance(self):
        print('Account no.:',self.account_no)
        print('Balance: ','Rs',self.balance)

account_no=int(input('Enter your account number: '))
balance=0

account=bank_accound(account_no,balance)
print('1.Deposit\n2.Withdraw\n3.Check Balance\n')
while True:
    choose=input('Choose any one option to continue: ')
    if choose=='1':
        amount_to_deposit=int(input('Enter the amount to deposit:'))
        account.deposit(amount_to_deposit)
    elif choose=='2':
        amount_to_withdraw=int(input('Enter the amount to withdraw: '))
        account.withdraw(amount_to_withdraw)
    elif choose=='3':
        account.display_balance()
    else:
        print('Invalid choice, Please type valid option :)')
    
    again=input('Do you want to perfrom another action(yes/no):')
    if again=='yes':
        continue
    else:
        break
'''
#Q4
'''
class employee:
    def __init__(self, name, salary, year_of_service):
        self.name= name
        self.salary= salary
        self.year_of_service= year_of_service
    def calculate_bonus(self):
        total_bonus=0.05*self.year_of_service
        bonus= total_bonus*self.salary
        return bonus

employees=[]

while True:
    name=input('Enter Employee Name: ')
    salary=int(input('Enter the Salary amount of this employee: '))
    year_of_service=int(input('Enter the number of year of service: '))
    E1=employee(name, salary, year_of_service)
    employees.append(employee)

    choose=input('Do you want to add more Employee? (yes/no): ')
    if choose != 'yes':
        break
for employee in employees:
    print('Employee Name: ', E1.name)
    print('Salary: ', E1.salary)
    print('Year of Service: ', E1.year_of_service)
    print('Total Annual Bonus: ', E1.calculate_bonus())
    print()

'''
#Q5
import pickle
class bank_account:
    def __init__(self,account_no,balance=0):
        self.account_no=account_no
        self.balance=balance
        self.transaction=[]

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            self.transaction.append(('Total Deposit:',amount))
        else:
            print('Invalid INPUT')
    
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            self.transaction.append(('Total withdraw:',amount))
        else:
            print('Invalid INPUT')   
            
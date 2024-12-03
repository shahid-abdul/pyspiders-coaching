from process import Bank,Postoffice

# g1 = GooglePay()
# g1.payment('abdul',100)

user = input('Where are you are going to make your investment: \n 1.Bank \t 2.Postoffice \n').lower()

name = input('name: ')
years = int(input('years: '))
amount = int(input('amount: '))
age = int(input('age: '))

if user == 'bank': 
    b1 = Bank()
    b1.interest(name,years,amount,age)
    b1.calculations()

elif user == 'postoffice':
    p1 = Postoffice()
    p1.interest(name,years,amount,age)
    p1.calculations()
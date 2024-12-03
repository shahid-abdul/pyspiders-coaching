from abstract import FD_Account
# import random

# class GooglePay:
#     def payment(self,name,amount):
#         print(name,'You made a transaction of Rs.',amount)
#         print('You won a cashback of Rs.',random.randint(1,50))

class Bank(FD_Account):
    def interest(self,name,years,amount,age):
        self.name = name
        self.years = years
        self.amount = amount
        self.age = age
    
    def calculations(self):
        if self.age > 60:
            if self.years >= 5:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (14.5/100)
                print('The total returns you will Rs.',(investment+returns))
            elif self.years > 2 and self.years < 5:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (11.5/100)
                print('The total returns you will Rs.',(investment+returns))
            else:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (9.5/100)
                print('The total returns you will Rs.',(investment+returns))
        else:
            if self.years >= 5:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (11.5/100)
                print('The total returns you will Rs.',(investment+returns))
            elif self.years > 1 and self.years < 5:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (9.5/100)
                print('The total returns you will Rs.',(investment+returns))
            else:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (7.5/100)
                print('The total returns you will Rs.',(investment+returns))


class Postoffice(FD_Account):
    def interest(self,name,years,amount,age):
        self.name = name
        self.years = years
        self.amount = amount
        self.age = age
    
    def calculations(self):
        if self.age > 60:
            if self.years >= 5:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (14.5/100)
                print('The total returns you will Rs.',(investment+returns))
            elif self.years > 2 and self.years < 5:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (11.5/100)
                print('The total returns you will Rs.',(investment+returns))
            else:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (9.5/100)
                print('The total returns you will Rs.',(investment+returns))
        else:
            if self.years >= 5:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (11.5/100)
                print('The total returns you will Rs.',(investment+returns))
            elif self.years > 1 and self.years < 5:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (9.5/100)
                print('The total returns you will Rs.',(investment+returns))
            else:
                investment = self.years * 12 * self.amount
                returns = self.years * 12 * self.amount * (7.5/100)
                print('The total returns you will Rs.',(investment+returns))




#Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print ("User details")
        print ("")
        print(f"Name:  = {self.name}")
        print(f'age:   = {self.age}')
        print(f'gender = {self.gender}')

#Child class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,value):
        self.balance = self.balance + value
        print(f'Your Account Balance is : ${self.balance}')

    def withdraw (self,amount):
        self.amount = amount
        if self.amount>self.balance:
            print(f'Insufficient Funds, Account balance is {self.balance}')

        else:
            self.balance = self.balance - amount

            print (f'Your remaining Account Balance is : ${self.balance}')

    def view_balance(self):
        self.show_details()
        print(f'Your remaining Account Balance is : ${self.balance}')



suhas = Bank("Suhas",26,"male")
suhas.deposit(200)
# suhas.deposit(200)
suhas.withdraw(250)
suhas.view_balance()




#OOP -Classes - Blueprints for objects
class Animal:
    #name
    #age
    #species

#add dynamic attributes for properties
    def __init__(self, name, age, species):
        self.name = name 
        self.age = age
        self.species = species

rose = Animal("Rose", 5, "Dog")
sparky = Animal("Sparky", 3, "Cat")
print(rose)


print(rose.name)
print(rose.age)
print(rose.species)

print(sparky)
print(sparky.name)
print(sparky.age)
print(sparky.species)

#-----------------------------

#in JavaScript
# b1 = {accountHolder: "John Doe", balance: 1000}
# b2 = {accountHoldAE: "Jane Doe", balance: 2000}  this is more error prone! 

class BankAccount:
    #instance variables or properties that describe our objects
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    #behaviors
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        self.balance -= amount
        return f"Withdrew ${amount: .2f}. New balance is ${self.balance: .2f}"

    def check_balance(self):
        return f"Your current balance is ${self.balance: .2f}"

ix = BankAccount("Ix", 1000)
rose = BankAccount("Rose", 200000)
tom = BankAccount("Tom", 9000)

print(ix.account_holder)
print(ix.balance)
ix.deposit(90)
print(ix.check_balance())
print(ix.withdraw(100))



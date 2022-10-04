"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, pay, hours=0):
        self.name = name
        self.contract = contract
        self.pay = pay
        self.hours = hours
        self.bonus = 0
        self.commission = 0
        self.NoOfContracts = 0

    def get_pay(self):
        amount = 0
        if self.contract == "salary":
            amount += self.pay
        elif self.contract == "hourly":
            amount += self.pay * self.hours

        if self.bonus:
            amount += self.bonus
        elif self.commission and self.NoOfContracts:
            amount += self.commission * self.NoOfContracts

        return amount


    def addBonus(self, amount):
        self.bonus += amount

    def addCommission(self, amount):
        self.commission += amount

    def setNoContracts(self, amount):
        self.NoOfContracts = amount

    def getBonus(self):
        return self.bonus

    def getCommission(self):
        return self.commission

    def getNoOfContracts(self):
        return self.NoOfContracts


    def __str__(self):
        msg = ""
        if self.contract == 'salary' and self.commission == 0 and self.bonus == 0:
            msg=f"{self.name} works on a monthly salary of {self.pay}. Their total pay is {self.get_pay()}."
        elif self.contract == 'hourly' and self.commission == 0 and self.bonus == 0:
            msg=f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour. Their total pay is {self.get_pay()}."
        elif self.contract == 'salary' and self.commission == 0 and self.bonus > 0:
            msg=f"{self.name} works on a monthly salary of {self.pay} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
        elif self.contract == 'hourly' and self.commission == 0 and self.bonus > 0:
            msg=f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
        elif self.contract == 'salary' and self.commission > 0 and self.bonus == 0:
            msg=f"{self.name} works on a monthly salary of {self.pay} and receives a commission for {self.NoOfContracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."
        elif self.contract == 'hourly' and self.commission > 0 and self.bonus == 0:
            msg=f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour and receives a commission for {self.NoOfContracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."


        return msg




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'salary', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'salary', 3000)
renee.addCommission(200)
renee.setNoContracts(4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 25, 150)
jan.addCommission(220)
jan.setNoContracts(3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'salary', 2000)
robbie.addBonus(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 30, 120)
ariel.addBonus(600)
print(str(ariel))

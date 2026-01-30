### parent Class for Bank Account
class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    ## Implementing Encapsulation
    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"BankAccount : \naccount_holder={self.account_holder}, \naccount_number={self.account_number}, \nbalance={self.get_balance()}"
    
### child class for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, initial_balance=0, interest_rate=0.23):
        super().__init__(account_holder, account_number, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        return interest

    def __str__(self):
        return f"SavingsAccount : \naccount_holder={self.account_holder}, \naccount_number={self.account_number}, \nbalance={self.get_balance()}, \ninterest_rate={self.interest_rate}"
    
### child class for Checking Account
class CheckingAndWithdrawingAccount(BankAccount):
    def __init__(self, account_holder, account_number, initial_balance=0, overdraft_limit=500):
        super().__init__(account_holder, account_number, initial_balance)
        self.overdraft_limit = overdraft_limit
    
    ## # Method overriding
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            current_balance = self.get_balance()
            if amount > current_balance:
                overdraft_used = amount - current_balance
                self._BankAccount__balance = 0  # Accessing the private variable
                self.overdraft_limit -= overdraft_used
            else:
                self._BankAccount__balance -= amount  # Accessing the private variable
            return True
        return False

    def __str__(self):
        return f"CheckingAndWithdrawingAccount : \naccount_holder={self.account_holder}, \naccount_number={self.account_number}, \nbalance={self.get_balance()}, \noverdraft_limit={self.overdraft_limit}"
    

## Object Creation:
Acc_1 = BankAccount("Anubhab", "123456789", 10000)
Acc_1_Savings = SavingsAccount(Acc_1, 0.05)
Acc_1_Checking = CheckingAndWithdrawingAccount(Acc_1, 500)

print(Acc_1,end="\n\n")
print(Acc_1_Savings,end="\n\n")
print(Acc_1_Checking,end="\n\n")

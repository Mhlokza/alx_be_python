class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = account_balance
        self.account_balance = 0
        
    def deposit(self,amount):
        self.account_balance+=amount

    def withdraw(self,amount):
        deduction = self.account_balance-amount
        if deduction<0:
            return False
        else:
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
        
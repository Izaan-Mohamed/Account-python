class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"{self.name} has insufficient funds.")
        self.balance -= amount

    def __str__(self):
        return f"{self.name} Balance: ${self.balance:,.2f}"


def transfer_funds(sender, receiver, amount, fee_account, fee_percent=0.05):
    fee = amount * fee_percent
    total_deduction = amount + fee

    print(f"\nTransferring ${amount:,.2f} from {sender.name} to {receiver.name} with ${fee:,.2f} fee to {fee_account.name}")
    
    sender.withdraw(total_deduction)
    receiver.deposit(amount)
    fee_account.deposit(fee)

    print("Transfer complete.")



account_A = Account("Account A", 50000)
account_B = Account("Account B", 10000)
account_C = Account("Account C (Fee Collector)", 0)


print("Initial Balances:")
print(account_A)
print(account_B)
print(account_C)


try:
    transfer_amount = 10000  
    transfer_funds(account_A, account_B, transfer_amount, account_C)
except ValueError as e:
    print(f"Error: {e}")


print("\nFinal Balances:")
print(account_A)
print(account_B)
print(account_C)

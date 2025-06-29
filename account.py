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
    total = amount + fee

    print(f"\nTransferring ${amount:,.2f} from {sender.name} to {receiver.name}...")
    print(f"Transaction fee of ${fee:,.2f} goes to {fee_account.name}.")

    sender.withdraw(total)
    receiver.deposit(amount)
    fee_account.deposit(fee)

    print("Transaction successful!\n")


def main():

    account_A = Account("Account A", 50000)
    account_B = Account("Account B", 10000)
    account_C = Account("Account C (Fee Collector)", 0)

    print("Welcome to the Account Transfer System!\n")

    while True:
     
        print(account_A)
        print(account_B)
        print(account_C)

        try:
            user_input = input("\nEnter amount to transfer from A to B (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting. Goodbye!")
                break

            amount = float(user_input)

            if amount <= 0:
                print("Amount must be positive.")
                continue

            transfer_funds(account_A, account_B, amount, account_C)

        except ValueError as e:
            print(f"Error: {e}")

        print("-" * 40)


if __name__ == "__main__":
    main()

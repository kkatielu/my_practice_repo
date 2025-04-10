from bank_account import BankAccount

account1 = BankAccount("1234", 1000)
print(account1)
account1.deposit(1000)
account1.withdraw(200)
print(account1.get_balance())

account2 = BankAccount("9876", 200)
print(account2)
account2.withdraw(300)
print(account2)
account2.withdraw(100)
print(account2)
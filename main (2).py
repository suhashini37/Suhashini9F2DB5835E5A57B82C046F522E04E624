class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      return True
    else:
      return False

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      return True
    else:
      return False

  def display_balance(self):
    return self.__account_balance


# Testing the BankAccount class
bank_account = BankAccount("123456789", "John Doe", 1000)
print("Initial balance:", bank_account.display_balance())

# Deposit money
bank_account.deposit(500)
print("Balance after deposit:", bank_account.display_balance())

# Withdraw money
bank_account.withdraw(200)
print("Balance after withdrawal:", bank_account.display_balance())

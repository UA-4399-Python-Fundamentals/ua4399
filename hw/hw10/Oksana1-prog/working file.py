
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.__account_number = account_number
        self.__balance = balance
        self._account_holder = account_holder

    @property
    def account_holder(self):
        return self._account_holder

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount:.2f}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.__balance


# Running the test as per your description:

my_account = BankAccount("123456789", "John Doe", 1000.0)
print(my_account.account_holder)

try:
    _ = my_account.__account_number
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

try:
    _ = my_account.__balance
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")
print(my_account.check_balance())
my_account.deposit(500.0)
print(my_account.check_balance())
my_account.withdraw(250.0)
print(my_account.check_balance())
try:
    my_account.account_holder = "Jane Doe"
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

my_account.withdraw(5000.0)
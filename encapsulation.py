class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute
    
    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <=0 :
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
class PaymentProcessor:
    def __init__(self, card_number, amount):
        self.__card_number = self.__mask_card_number(card_number)
        self.__amount = amount

    def __mask_card_number(self, card_number):
        return "****-****-****-" + card_number[-4:]

    def process_payment(self):
      print(f"Processing payment of {self.__amount} for card {self.__card_number}")

if __name__ == "__main__":
   payment = PaymentProcessor("1234567812345678", 250.00)
   payment.process_payment()
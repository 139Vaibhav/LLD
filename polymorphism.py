from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")

class UPIProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing UPI payment of ₹{amount}")

if __name__ == "__main__":
    processors = [
        CreditCardProcessor(),
        PayPalProcessor(),
        UPIProcessor()
    ]

    for processor in processors:
        processor.process_payment(100.0)
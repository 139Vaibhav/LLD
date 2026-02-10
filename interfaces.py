from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(self, amount):
        pass

    @abstractmethod
    def refund_payment(self, amount):
        pass

class StripePayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via Stripe {amount}")

    def refund_payment(self, amount):
        print(f"Refunding payment via Stripe {amount}")

class PayPalPayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via PayPal {amount}")

    def refund_payment(self, amount):
        print(f"Refunding payment via PayPal {amount}")

class CheckoutService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def set_payment_gateway(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def checkout(self, amount):
        self.payment_gateway.initiate_payment(amount)

    def refund(self, amount):
        self.payment_gateway.refund_payment(amount)

if __name__ == "__main__":
    stripe = StripePayment()
    checkout_service = CheckoutService(stripe)
    checkout_service.checkout(100)
    checkout_service.refund(50)
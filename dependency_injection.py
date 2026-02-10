from abc import ABC, abstractmethod

class Sender(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

class NotificationService:
    def __init__(self, sender: Sender) -> None:
        self.sender = sender

    def notify(self, message: str) -> None:
        self.sender.send(message)

if __name__ == "__main__":
    class EmailSender(Sender):
        def send(self, message: str) -> None:
            print(f"Sending Email: {message}")

    class SMSSender(Sender):
        def send(self, message: str) -> None:
            print(f"Sending SMS: {message}")

    email_service = NotificationService(EmailSender())
    email_service.notify("Hello via Email!")

    sms_service = NotificationService(SMSSender())
    sms_service.notify("Hello via SMS!")
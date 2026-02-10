from enum import Enum

class orderStatus(Enum):
    PLACED = "PLACED"
    CONFIRMED = "CONFIRMED"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"

class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25

    def __init__(self, value):
        self.coin_value = value
    
    def get_value(self):
        return self.coin_value

if __name__ == "__main__":
    status = orderStatus.SHIPPED

    if status == orderStatus.SHIPPED:
        print("Your package is on the way!")

    coin = Coin.QUARTER.get_value() + Coin.DIME.get_value()
    print(f"Total coin value: {coin} cents")
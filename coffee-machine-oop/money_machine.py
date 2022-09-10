###############################################################################
# @file     money_machine.py
# @brief    Implement MoneyMachine class
#
# Create constructor
# Implement eport(), process_coins() ,and make_payment() methods.
#
# @author   Katsuki Oike
# @date     September 10, 2022
###############################################################################

class MoneyMachine:

    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    # Print the current profit
    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    # Return the total calculated from coins inserted
    def process_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    # Return True when payment is accepted, or False if insufficient
    def make_payment(self, cost):
        self.process_coins()
        can_pay = True
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            can_pay = False
        return can_pay

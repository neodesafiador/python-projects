###############################################################################
# @file     coffee_maker.py
# @brief    Models the machine that makes the coffee
#
# Create constructor
# Implement report(), is_resource_sufficient(), and make_coffee() methods.
#
# @author   Katsuki Oike
# @date     September 10, 2022
###############################################################################

class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    # Print a report of all resources
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    # Return True when order can be made, False if ingredients are insufficient
    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    # Deduct the required ingredients from the resources
    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

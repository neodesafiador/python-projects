###############################################################################
# @file     main.py
# @brief    Make a digital version of coffee machine in OOP
#
# Program Requirements
# 1. Print report.
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make Coffee.
#
# @author   Katsuki Oike
# @date     September 10, 2022
###############################################################################

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
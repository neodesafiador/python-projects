###############################################################################
# @file     main.py
# @brief    Make a digital version of coffee machine
#
# Program Requirements
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#    a. Check the user’s input to decide what to do next.
#    b. The prompt should show every time action has completed, e.g. once the
#       drink is dispensed. The prompt should show again to serve the next
#       customer.
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
#    a. For maintainers of the coffee machine, they can use “off” as the secret
#       word to turn off the machine. Your code should end execution when this
#       happens.
# 3. Print report.
#    a. When the user enters “report” to the prompt, a report should be
#       generated that shows the current resource values. e.g.
#       Water: 100ml  Milk: 50ml  Coffee: 76g  Money: $2.5
# 4. Check resources sufficient?
#    a. When the user chooses a drink, the program should check if there are
#       enough resources to make that drink.
#    b. Ex) If Latte requires 200ml water but there is only 100ml left in the
#       machine. It should not continue to make the drink but print: “Sorry
#       there is not enough water.”
#    c. The same should happen if another resource is depleted.
# 5. Process coins.
#    a. If there are sufficient resources to make the drink selected, then the
#       program should prompt the user to insert coins.
#    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05,
#       pennies = $0.01
#    c. Calculate the monetary value of the coins inserted. Ex) 1 quarter,
#       2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
#    a. Check that the user has inserted enough money to purchase the drink
#       they selected. Ex) Latte cost $2.50, but they only inserted $0.52 then
#       after counting the coins the program should say “Sorry that's not enough
#       money. Money refunded.”.
#    b. But if the user has inserted enough money, then the cost of the drink
#       gets added to the machine as the profit and this will be reflected the
#       next time “report” is triggered.
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
#    c. If the user has inserted too much money, the machine should offer
#       change. Ex) “Here is $2.45 dollars in change.” The change should be
#       rounded to 2 decimal places.
# 7. Make Coffee.
#    a. If the transaction is successful and there are enough resources to make
#       the drink the user selected, then the ingredients to make the drink
#       should be deducted from the coffee machine resources.
#       report before purchasing latte:
#       Water: 300ml
#       Milk: 200ml
#       Coffee: 100g
#       Money: $0
#       Report after purchasing latte:
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
#    b. Once all resources have been deducted, tell the user “Here is your
#       latte. Enjoy!”. If latte was their choice of drink.
#
# @author   Katsuki Oike
# @date     September 10, 2022
###############################################################################

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


# Return True when order can be made, False if ingredients are insufficient
def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


# Return the total calculated from coins inserted
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# Return True when the payment is accepted, or False if money is insufficient
def is_transaction_successful(money_received, drink_cost):
    is_success = True
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        is_success = False
    return is_success


# Deduct the required ingredients from the resources
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
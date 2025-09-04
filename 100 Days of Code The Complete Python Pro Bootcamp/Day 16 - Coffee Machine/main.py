# -*- coding: utf-8 -*-

"""
100 Days of Code The Complete Python Pro Bootcamp for 2023
Day 16 - Intermediate - Object Oriented Programming (OOP)

Project: Coffee Machine

Created on Mon Sep 01 18:32:02 2025

Coffee Machine Documentation:
https://replit.com/@appbrewery/oop-coffee-machine-start
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()




def coffee_machine():
    # Instantiate variable for loop (not "off")
    not_off = True
    # Instantiate variable for tracking gross earnings
    global revenue
    revenue = 0

    # Start the loop
    while not_off == True:
        options = menu.get_items()
        # 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino/):
        # Instantiate variable for user order
        # Prompt user for order
        order = input("What would you like? ({options}): ").lower()

        # If Else Conditions for menu options
        if order == "off":
            # 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
            not_off = False
        elif order == "report":
            # 3. Print report.
            # a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
            # Print out current inventory of resources
            coffee_maker.report()  # Prints a report of all resources.
            money_machine.report()  # Prints the current profit
        else:
            # Call payment function
            # Check if resources sufficient
            if payment(order) and check_inventory(order):
                # TODO: 7. "Deliver" drink with a print statement
                # "Deliver" drink order
                print(f"Here is your {order}. Enjoy!")
                # Deduct ingredients of selection from current resources
                update_inventory(order)
            else:
                # Break loop if payment insufficient
                coffee_machine()

if __name__ == "__main__":
    coffee_machine()




# 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino/):
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.


# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not
# continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
coffee_maker.is_resource_sufficient(drink)














# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected. E.g
# Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program
# should say “ Sorry that's not enough money. Money refunded. ”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.


# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the user
# selected, then the ingredients to make the drink should be deducted from the coffee
# machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte
# was their choice of drink.




#%%

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


# Create function to check inventory
def check_inventory(order):
    # print(f"check_inventory order: ", order)
    # Compare each ingredient amount to inventory amount
    for ingredient, amount in MENU[order]["ingredients"].items():
        if amount > resources[ingredient]:
            print(f"Sorry, there's not enough {ingredient}.")
            return False
    return True

# Create function for payment
def payment(order):
    global revenue
    # Instantiate variable for the cost the drink ordered
    cost = MENU[order]["cost"]

    # TODO: 4. Prompt users for payment ("Please insert coins.")
    # Prompt user for payment
    print("Please insert coins.")

    # TODO: 5. Prompt user for quantity of each coin (Quarters, dimes, nickles, pennies)
    # Prompt user for quantity of each coin
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    # Tally up payment
    total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    change = (total - cost)
    # TODO: 6. Return change ("Here is x in change.)
    # Compare payment to cost
    if change > 0:
        # If greater than cost, "return change" and return True
        print(f"Here is ${change:.2} in change.")
        revenue += cost
        return True
    # If equal to cost return True
    elif change == 0:
        revenue += cost
        return True
    # If less than cost return False
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def update_inventory(order):
    # Deduct ingredients of selection from current resources
    for ingredient, amount in MENU[order]["ingredients"].items():
        resources[ingredient] -= amount

def coffee_machine():
    # Instantiate variable for loop (not "off")
    not_off = True
    # Instantiate variable for tracking gross earnings
    global revenue
    revenue = 0

    # TODO: 8. Repeat loop
    # Start the loop
    while not_off == True:
        # TODO: 2. Prompt user for order ("What would you like? (espresso/latte/cappuccino)
        # Instantiate variable for user order
        # Prompt user for order
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # If Else Conditions for menu options
        if order == "report":
            # TODO: 1. Print report of resources left
            # Print out current inventory of resources
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${revenue}")
        elif order == "off":
            not_off = False
        else:
            # Call payment function
            # Check if resources sufficient
            if payment(order) and check_inventory(order):
                # TODO: 7. "Deliver" drink with a print statement
                # "Deliver" drink order
                print(f"Here is your {order}. Enjoy!")
                # Deduct ingredients of selection from current resources
                update_inventory(order)
            else:
                # Break loop if payment insufficient
                coffee_machine()

if __name__ == "__main__":
    coffee_machine()


"""
Coffee Machine Program Requirements

1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    a. Check the user’s input to decide what to do next.
    b. The prompt should show every time action has completed, e.g. once the drink is
        dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
        the machine. Your code should end execution when this happens.
3. Print report.
    a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5
4. Check resources sufficient?
    a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
        not continue to make the drink but print: “ Sorry there is not enough water. ”
    c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
    a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. 
        E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
    a. Check that the user has inserted enough money to purchase the drink they selected.
        E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
        program should say “ Sorry that's not enough money. Money refunded. ”.
    b. But if the user has inserted enough money, then the cost of the drink gets added to the
        machine as the profit and this will be reflected the next time “report” is triggered. E.g.
            Water: 100ml
            Milk: 50ml
            Coffee: 76g
            Money: $2.5
    c. If the user has inserted too much money, the machine should offer change.
        E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
7. Make Coffee.
    a. If the transaction is successful and there are enough resources to make the drink the
    user selected, then the ingredients to make the drink should be deducted from the
    coffee machine resources.
    E.g. report before purchasing latte:
        Water: 300ml
        Milk: 200ml
        Coffee: 100g
        Money: $0
    Report after purchasing latte:
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5
    b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
"""

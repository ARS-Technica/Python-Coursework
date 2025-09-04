# -*- coding: utf-8 -*-
"""
100 Days of Code The Complete Python Pro Bootcamp for 2023
Day 16 - Intermediate - Object Oriented Programming (OOP)

Project: Coffee Machine

Created on Mon Sep 01 18:32:02 2025

Coffee Machine Documentation:
https://replit.com/@appbrewery/oop-coffee-machine-start
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


def coffee_machine():
    # Instantiate variable for loop (not "off")
    not_off = True

    # Start the loop
    while not_off:
        # Create object from menu
        options = menu.get_items()
        # 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino/):

        # Prompt user for order
        order = input(f"What would you like? ({options}): ").lower()

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
            # Create object to represent drink order
            drink = menu.find_drink(order)

            # 4. Check resources sufficient?
            if coffee_maker.is_resource_sufficient(drink):
                # coffee_maker.make_coffee(drink)
                # 5. Process coins.
                print(f"That will be ${drink.cost:.2f}, please.")
                if money_machine.make_payment(drink.cost):
                # Returns True when payment is accepted, or False if insufficient.
                    # 7. Make Coffee.
                    coffee_maker.make_coffee(drink)
                    # Deducts the required ingredients from the resources.


if __name__ == "__main__":
    coffee_machine()


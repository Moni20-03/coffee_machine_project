from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
coins = MoneyMachine()

machine_is_on = True

while machine_is_on:
    user_choice = input(f"What would you like? {menu.get_items()}: ").lower()

    if user_choice == "off":
        machine_is_on = False
    elif user_choice == "report":
        coffee.report()
        coins.report()
    else:
        item = menu.find_drink(user_choice)
        if coffee.is_resource_sufficient(item) and coins.make_payment(item.cost):
                coffee.make_coffee(item)
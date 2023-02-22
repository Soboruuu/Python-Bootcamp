from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
options = menu.get_items()

is_turned_off = False

while not is_turned_off:
    order = input(f"What would you like? {options}: ").lower()
    if order == "off":
        is_turned_off = True
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)

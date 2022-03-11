from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    menu_order = menu.get_items()
    order = input(f"What do you like? {menu_order}")
    if order == "off":
        machine_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "no":
        print("Bai bai")
        break
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




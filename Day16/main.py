from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
choice = True

while choice:
    choice = input(f"What would you like ({menu.get_items()}): ")
    if choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    elif choice == "off":
        choice = False
    else:
        coffee = menu.find_drink(choice)

        if coffeeMaker.is_resource_sufficient(coffee) and moneyMachine.make_payment(coffee.cost):

            coffeeMaker.make_coffee(coffee)

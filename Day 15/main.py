resources = {"water": 300, "coffee": 100, "milk": 200, "money_machine": 0}
menu = {
    "espresso": {"water": 50, "coffee": 18, "milk": 0, "price": 1.5},
    "latte": {"water": 200, "coffee": 24, "milk": 150, "price": 2.5},
    "capuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 3}
        }
coin = {
    "penny": 0.01,
    "dime": 0.1,
    "nickel": 0.05,
    "quarter": 0.25
        }

def coin_2_money(penny, dime, nickel, quarter):
    money = (penny*0.01)+(dime*0.1)+(nickel*0.05)+(quarter*0.25)
    return money

def is_material_avai(drink_material):
    if drink_material["water"] >= resources["water"] or drink_material["milk"] >= resources["milk"] or drink_material["coffee"] >= resources["coffee"]:
        print("Sorry we ran out of materia. Try another pls !!!")
        return False
    else:
        return True

def machine_material(water_material, milk_material, coffee_material, price):
    money_machine = 0
    water_left = resources["water"] - water_material
    milk_left = resources["milk"] - milk_material
    coffee_left = resources["coffee"] - coffee_material
    money_machine += price
    resources_left = {"water": water_left, "coffee": coffee_left, "milk": milk_left, "money_machine": price}
    return resources_left

def machine_report(resources_left):
    water_report = resources_left["water"]
    milk_report = resources_left["milk"]
    coffee_report = resources_left["coffee"]
    money_report = resources_left["money_machine"]
    print(f"Water: {water_report}ml")
    print(f"Milk: {milk_report}ml")
    print(f"Coffee: {coffee_report}g")
    print(f"Money: {money_report}")

def drink_material(buyer_choice):
    if buyer_choice == "espresso":
        espresso_material = menu["espresso"]
        return espresso_material
    elif buyer_choice == "latte":
        latte_material = menu["latte"]
        return latte_material
    elif buyer_choice == "cappuccino":
        cappuccino_material = menu["capuccino"]
        return cappuccino_material
    else:
        print("Try another drink!!!")

water_material = 0
milk_material = 0
coffee_material = 0
price = 0
machine_on = True
while machine_on:
    buyer_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if buyer_choice == "report":
        resources_left = machine_material(water_material, milk_material, coffee_material, price)
        machine_report(resources_left)
    elif buyer_choice == "off":
        machine_on = False
        break
    else:
        drink_material = drink_material(buyer_choice)
        # print(drink_material)
        if is_material_avai(drink_material):
            print("Please insert coins!!!")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickel = int(input("How many nickels?: "))
            penny = int(input("How many pennies?: "))

            money_buyer = coin_2_money(penny, dime, nickel, quarter)
            # print(money_buyer)

            water_material = drink_material["water"]
            milk_material = drink_material["milk"]
            coffee_material = drink_material["coffee"]
            price = drink_material["price"]
            if money_buyer >= price:
               print(f"Here is ${money_buyer-price} in charge")
               resources_left = machine_material(water_material, milk_material, coffee_material, price)
               # machine_report(resources_left)
               print(f"Here is your {buyer_choice}")
            else:
               print("Pay more!!!")

        repeat_function = input("Do you want anything else? (y/n): ")
        if repeat_function == "n":
            machine_on = False

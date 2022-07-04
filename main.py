from menu import MENU
from inventory import resources

running = True


def process_order(order_name):
    resources_required = MENU[order_name]["ingredients"]
    resources_available = 0
    drink_cost = MENU[order_name]["cost"]

    for resource in resources_required:
        if resources[resource] >= resources_required[resource]:
            resources_available += 1
        else:
            print(f"Sorry there is not enough {resource}.")

    if resources_available == len(resources_required):
        print(f"The price of your drink is ${drink_cost}.")
        print("Please insert coins.")

        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        paid = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

        if paid > drink_cost:
            change = round(paid - drink_cost, 2)
            profit = paid - change
            print(f"Here is ${change} in change.")

            resources["money"] += profit
            make_drink(order_name)
        elif paid == drink_cost:
            resources["money"] += paid
            make_drink(order_name)
        else:
            print("Sorry, that's not enough money. Money refunded.")


def make_drink(drink):
    ingredients = MENU[drink]["ingredients"]

    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

    print(f"Here's your {drink}. Enjoy! ☕")


while running:
    order = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        running = False
    elif order == "report":
        print(f"""
        Water: {resources['water']}ml
        Milk: {resources['milk']}ml
        Coffee: {resources['coffee']}g
        Money: ${resources['money']}
        """)
    elif order == "espresso":
        process_order(order)
    elif order == "latte":
        process_order(order)
    elif order == "cappuccino":
        process_order(order)
    else:
        print("Invalid drink! Please try again.")

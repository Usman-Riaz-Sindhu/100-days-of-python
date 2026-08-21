class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 50, 0, 18, 1.5),
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("cappuccino", 250, 100, 24, 3.0)
        ]

    def get_items(self):
        return "/".join([item.name for item in self.menu])

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item

        return None


class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False

        return True

    def make_coffee(self, drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]

        print(f"Here is your {drink.name}. Enjoy!")


class MoneyMachine:
    CURRENCY = "$"

    COINS = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("Please insert coins.")

        total = 0

        for coin in self.COINS:
            count = int(input(f"How many {coin}? "))
            total += count * self.COINS[coin]

        return total

    def make_payment(self, cost):
        payment = self.process_coins()

        if payment >= cost:
            change = round(payment - cost, 2)

            print(
                f"Here is {self.CURRENCY}{change} in change."
            )

            self.profit += cost

            return True

        print("Sorry, that's not enough money. Money refunded.")
        return False


# Objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


machine_on = True

while machine_on:

    choice = input(
        f"What would you like? ({menu.get_items()}): "
    ).lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)

        if drink is None:
            print("Sorry, that drink is not available.")

        elif coffee_maker.is_resource_sufficient(drink):

            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
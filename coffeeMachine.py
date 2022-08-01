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


def is_sufficient(drink):
    """If sufficient resources, then return True, otherwise False"""
    for k, v in drink['ingredients'].items():
        if resources[k] - v < 0:
            print('Sorry there is not enough ' + k + ' .')
            return False
        else:
            return True


def process_coins():
    """ calculate the amount of coins inserted"""
    print('Please insert coins.')
    print('How many quarters?: ')
    quarters = input()
    print('How many dimes?: ')
    dimes = input()
    print('How many nickles?: ')
    nickles = input()
    print('How many pennies?: ')
    pennies = input()

    moneyInserted = (int(quarters) * 0.25) + (int(dimes) * 0.10) + (int(nickles) * 0.05) + (
            int(pennies) * 0.01)

    return moneyInserted


def enough_money(moneyInserted, drink):
    """ if enough money inserted then return True, else return False"""
    itemCost = drink['cost']
    global money
    if moneyInserted < itemCost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif moneyInserted > itemCost:
        change = moneyInserted - itemCost
        print('Here is $ {:0.2f} dollars in change.'.format(change))  # round to two decimal
        # place
        money += itemCost
        return True
    elif moneyInserted == itemCost:
        money += itemCost
        return True


def make_coffee(drink):
    """ deduct the ingredients from the coffee machine resource"""
    for k, v in drink['ingredients'].items():
        resources[k] = resources[k] - v
    print('Here is your ' + choice + ' ☕️. Enjoy!')


machineOn = True
money = 0.0
while machineOn:
    print('What would you like? (espresso/latte/cappuccino):')
    choice = input()
    if choice == 'off':
        machineOn = False
        break
    elif choice == 'report':
        print('Water: ' + str(resources['water']) + 'ml')
        print('Milk: ' + str(resources['milk']) + 'ml')
        print('Coffee: ' + str(resources['coffee']) + 'g')
        print('Money: $' + str(money))
    else:
        drink = MENU[choice]
        if is_sufficient(drink):
            moneyInserted = process_coins()
            if enough_money(moneyInserted, drink):
                make_coffee(drink)

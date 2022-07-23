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

# prompt user
machineOn = True
money = 0.0
while machineOn:
    print('What would you like? (espresso/latte/cappuccino):')
    choice = input()
    if choice == 'off':
        machineOn = False
        break
    if choice == 'report':
        print('Water: ' + str(resources['water']) + 'ml')
        print('Milk: ' + str(resources['milk']) + 'ml')
        print('Coffee: ' + str(resources['coffee']) + 'g')
        print('Money: $' + str(money))
        continue

    enough = True

    if enough:
        # check resources sufficient
        for k, v in MENU[choice]['ingredients'].items():
            if resources[k] - v < 0:
                print('Sorry there is not enough ' + k + ' .')
                enough = False
                break

    if enough:
        # process coins
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

        itemCost = MENU[choice]['cost']
        if moneyInserted < itemCost:
            print("Sorry that's not enough money. Money refunded.")
            enough = False
        elif moneyInserted > itemCost:
            change = moneyInserted - itemCost
            print('Here is $ {:0.2f} dollars in change.'.format(change))  # round to two decimal
            # place

        if enough:
            for k, v in MENU[choice]['ingredients'].items():
                resources[k] = resources[k] - v
            money += itemCost
            print('Here is your ' + choice + ' ☕️. Enjoy!')

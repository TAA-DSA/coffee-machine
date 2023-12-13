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

resources['money'] = 0


# ask_prompt = input("What would you like? (espresso/latte/cappuccino) : ").lower()
# def report(ask_prompt, resources):

def is_sufficient_resources(ingredients):
    for items in ingredients:
        if ingredients[items] >= resources[items]:
            print(f'Sorry not enough {ingredients[items]}')
            return False
        return True


def cost_check(ask_quarters, ask_dimes, ask_nickles, ask_pennies, drink):
    # print(ask_quarters, ask_dimes, ask_nickles, ask_pennies, drink)
    total = (0.25 * ask_quarters) + (0.10 * ask_dimes) + (0.05 * ask_nickles) + (0.01 * ask_pennies)
    if total < drink:
        print('Sorry not enough money. Money refunded')
        return False
    elif total == drink:
        resources['money'] += drink
        return True
    else:
        refund = total - drink
        resources['money'] += drink
        print(f'Here is ${refund} in change')
        return True


def make_coffee(drink, ask_prompt):
    for values in drink:
        resources[values] -= drink[values]
    print(f'Here is your {ask_prompt}. Enjoy!')


def coffee_machine_start():
    start_machine = True
    while start_machine:
        ask_prompt = input("What would you like? (espresso/latte/cappuccino) : ").lower()

        if ask_prompt == 'report':
            # loop through the dictionary using items to print the key value pair
            # add units to values
            for items, value in resources.items():
                item_units = {
                    'Water': 'ml',
                    'Milk': 'ml',
                    'Coffee': 'mg',
                }
                selected_items = items[0].upper() + items[slice(1, len(items))]

                if selected_items in item_units:
                    unit = item_units[selected_items]
                    print(f'{selected_items} : {value} {unit}')
                elif selected_items == 'Money':
                    print(f'{selected_items} : $ {value} ')

        elif ask_prompt == 'espresso' or ask_prompt == 'latte' or ask_prompt == 'cappuccino':

            # ask user for money in quarter, dimes, nickles, pennies
            drink = MENU[ask_prompt]
            if (is_sufficient_resources(drink['ingredients'])):
                print('Please insert coins')
                ask_quarters = float(input('how many quarters?: '))
                ask_dimes = float(input('how many dimes?: '))
                ask_nickles = float(input('how many nickles?: '))
                ask_pennies = float(input('how many pennies?: '))
                if (cost_check(ask_quarters, ask_dimes, ask_nickles, ask_pennies, drink['cost'])):
                    make_coffee(drink['ingredients'], ask_prompt)
            else:
                print('Not enough resources available')
        elif ask_prompt == "off":
            start_machine = False
    if not start_machine:
        pass


coffee_machine_start()

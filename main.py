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

#TODO: Print report

dict_values = MENU['espresso'].values()
print(dict_values)
resources['money'] = 0
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

        if ask_prompt == 'espresso' or ask_prompt == 'latte' or ask_prompt == 'cappuccino':
            #ask user for money in quarter, dimes, nickles, pennies
            for key, value in MENU[ask_prompt].items():
                # check if resources are available to make the chosen drink

                print(key, value)
        elif ask_prompt == "off":
            start_machine = False
    if not start_machine:
        pass




coffee_machine_start()
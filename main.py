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

dict_values = MENU['espresso'].values()
print(dict_values)
resources['Money'] = 0
def coffee_machine_start():
    start_machine = True
    while start_machine:
        ask_prompt = input("What would you like? (espresso/latte/cappuccino) : ").lower()
        if ask_prompt == 'espresso' or ask_prompt == 'latte' or ask_prompt == 'cappuccino':
            for keys, value in MENU[ask_prompt].items():
                #check if resources are available to make the chosen drink
                print(keys, value)
        elif ask_prompt == 'report':
            # loop through the dictionary using items to print the key value pair
            for items, value in resources.items():


                print(f'{items}: {value} ')
        elif ask_prompt == "off":
            start_machine = False
    if not start_machine:
        pass




coffee_machine_start()
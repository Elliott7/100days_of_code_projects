"""
Project Number Fifteen - Coffee Machine
This project is about creating a coffee machine that takes multiple inputs, compares all of them to the
existing resource database and then either returns with objections or updates the database and gives them
their coffee.
"""

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


def users_coffee():
    """
    Gets the users coffee choice and returns it.

    :return user_input: Users choice of coffee
    """

    options = ['espresso', 'latte', 'cappuccino', 'off', 'report']
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino)\n")
        if user_input not in options:
            continue
        else:
            break
    return user_input


def check_resources(coffee_choice, resources):
    """
    Checks the resource database for the current coffees requirements.

    :param coffee_choice: Users choice of coffee
    :param resources: Resource database
    :return True or False:
    """
    data_to_check = MENU[coffee_choice]["ingredients"]
    available_water = data_to_check['water'] <= resources['water']
    available_coffee = data_to_check['coffee'] <= resources['coffee']
    if data_to_check.get('milk') is None:
        return all([available_coffee, available_water])
    else:
        available_milk = data_to_check['milk'] <= resources['milk']
        return all([available_coffee, available_water, available_milk])


def get_users_coins(coffee_type):
    """
    Collects the users coins, adds them up and then compares to the coffee cost. If there's not enough
    coins it returns 'Sorry that's not enough money. Money refunded'
    Return False if not enough money, or the amount if it is accurate

    :param coffee_type: Users choice of coffee
    :return total: This is how much the user has payed
    """

    coffee_cost = MENU[coffee_type]['cost']
    while True:
        try:
            quarters = int(input("How many quarters\n")) * .25
            dimes = int(input("How many dimes?\n")) * .10
            nickles = int(input("How many nickles?\n")) * .05
            pennies = int(input("How many pennies?\n")) * .01
            total = sum([quarters, dimes, nickles, pennies])
            break
        except ValueError:
            print('Please enter a valid number only')
    if coffee_cost > total:
        return False
    return total


def return_money(total_paid, coffee_choice):
    """
    Calculates the users change and gives it back to them.

    :param total_paid: The amount the user has entered
    :param coffee_choice: Users choice of coffee
    :return None
    """

    coffee_cost = MENU[coffee_choice]['cost']
    refund = total_paid - coffee_cost
    print(f"Here is ${refund:.2f} change.\nHere is your {coffee_choice} ☕")


def deduct_resources(coffee_choice, resource_log):
    """
    Takes the resources for that particular coffee and subtracts it from the available resources. Returns the
    resources dict to be saved as itself.

    :param coffee_choice: Users choice of coffee
    :param resource_log: Resources database
    :return resource_log: Updated resource database
    """

    coffee_details = MENU[coffee_choice]["ingredients"]
    resource_log['water'] = resource_log['water'] - coffee_details['water']
    resource_log['coffee'] = resource_log['coffee'] - coffee_details['coffee']

    if coffee_details.get("milk"):
        resource_log['milk'] = resource_log['milk'] - coffee_details['milk']

    return resource_log


def no_run(resource):
    """
    If there's no resources available for the lowest option then it will cancel out
    :param resource: Resources database
    :return bool:
    """
    if resource['coffee'] < 18 or resource['water'] < 50:
        print("Sorry, this machine is out of service.\nWe do not have enough stock for "
              "any of the available choices")
        return True


def print_resources_and_profit(resource, profit):

    for key, val in resource.items():
        if key == "water" or key == "milk":
            print(f"{key.title()}: {val}ml")
        else:
            print(f"{key.title()}: {val}g")
    print(f"Money: ${profit}")


def main():
    profit = 0
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    while True:
        if no_run(resources):
            break

        get_coffee_choice = users_coffee()

        if get_coffee_choice == "report":
            print_resources_and_profit(resources, profit)
            continue

        elif get_coffee_choice == "off":
            print("Turning machine off")
            break

        if not check_resources(get_coffee_choice, resources):
            print("Sorry there's not enough resources")
            continue

        total_paid = get_users_coins(get_coffee_choice)
        if not total_paid:
            print("Sorry that's not enough money. Your money has been refunded")
            continue

        return_money(total_paid, get_coffee_choice)
        profit += MENU[get_coffee_choice]['cost']
        resources = deduct_resources(get_coffee_choice, resources)

        continue


if __name__ == "__main__":
    main()

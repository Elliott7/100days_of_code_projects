"""
Project Number Two - Tip Calculator.
Takes in the cost of the meal, the number of payees and the tip percentage then returns
the individual cost for each person to pay
"""


def tip_calculator(cost, split, tip_percentage):
    """
    Calculates the the additional cost of tipping

        :param cost: (float) - Total bill cost
        :param split: (int) - Number of people splitting the bill
        :param tip_percentage: (int) - Tip percentage
        :return payment: (float) - Total amount to tip
    """
    payment = cost * (1 + tip_percentage/100) / split
    return payment


if __name__ == "__main__":
    print("Welcome to the tip calculator")
    total_cost = float(input("What was the total bill? "))
    split_amount = int(input("How many people to split the bill? "))
    tip_percent = int(input("What percentage tip would you like to give? "))
    individual_payment = tip_calculator(total_cost, split_amount, tip_percent)
    print(f"Each person should pay: ${round(individual_payment, 2)}")
''' Assignment: Vending machine

   PA2VendingMachine.py

   Name: Tayven Stover 

   File Created on February 11, 2024   
   Integrity is demonstrated at NOVA through adherence to principles and
    actions that foster accountability, honesty and trustworthiness;

'''
"""
    Components:
        - Currency deposit
        - Purchase item selection
        - Change return
    
    Currency deposit:
        - Accepts: penny, nickel, dime, quarter, dollar, and five dollars
        - User enters money, this will be simulated in a loop ex. - 0 to exit
            - user enters 1.00
            - user enters .75
            - user enters 0
            - user total: $1.75
    
    Purchase item selection:
        - User selects an item to purchase
        - User enters the product type ex. - 0 to exit
            - user enters 1
            - user enters 0
            - user total: $1.75
            - user selection: A
            - item cost: $1.00
            - user change: $0.75
    
    Change return:
        - User receives change
        
    
"""

CANCEL_REMINDER = "* At any point if you wish to cancel operation or return to the last menu, please enter 0. Thank you:"
class InputError(Exception):
        pass

def money_input(current_money = 0):
    LEGAL_DEPOSITS = [.01, .05, .10, .25, 1.0, 5.0]
    INPUT_PROMPT = (
        "If you would like to make a selection,\n"
        "please enter the appropriate currency into the machine.\n\n"
        "Please enter:\n"
        "1.00 for $1 bill\n"
        "5.00 for $5 bills\n"
        ".01 for pennies\n"
        ".05 for nickels\n"
        ".10 for dimes\n"
        ".25 for quarters\n"
        "0 to cancel\n\n"
        f"{CANCEL_REMINDER}\n\n"
    )

    while True:
        try: 
            user_deposit = float(input(INPUT_PROMPT))

            if user_deposit == 0:
                break
        
            elif user_deposit in LEGAL_DEPOSITS:
                current_money += user_deposit
            
            else:
                raise InputError
        except (ValueError, InputError):
            print('*' * 15, "Error: invalid input", '*' * 15)

    return current_money

def item_selection(user_money = 0):
    AVAILABLE_ITEMS = {
        1: ['Car', 1.00],
        2: ['House', 1.25],
        3: ['Pool', 1.50],
        4: ['Supercar', 1.75],
        5: ['Superhouse', 2.00],
    }
    item_price = 0

    while True:
        print('*' * 15, f"Total money in machine is ${user_money:.2f}", '*' * 15)
        print(CANCEL_REMINDER)

        for key in AVAILABLE_ITEMS:
            print(f"Product {AVAILABLE_ITEMS[key][0]} type '{key}', (Price = ${AVAILABLE_ITEMS[key][1]:.2f})")

        try:
            user_selection = int(input("Your entry is: "))

            if user_selection in AVAILABLE_ITEMS:
                print('*' * 15, f"The item cost is ${AVAILABLE_ITEMS[user_selection][1]:.2f}", '*' * 15)
                item_price = AVAILABLE_ITEMS[user_selection][1]
                break

            else:
                raise InputError

        except (ValueError, InputError):
            print('*' * 15, "Error: invalid input", '*' * 15)
    
    return item_price

def change_dispenser(user_money = 0, item_price = 0):
    difference = user_money - item_price
    if difference < 0:
        print('*' * 15, "Error: you don't have enough money\nDispensing change:\n", '*' * 15)

    else:
        user_money -= item_price
    
    dollars = user_money // 1
    user_money -= dollars
    quarters = round(user_money, 2) // .25
    user_money -= quarters * .25
    dimes = round(user_money, 2) // .10
    user_money -= dimes * .10
    nickels = round(user_money, 2) // .05
    user_money -= nickels * .05
    pennies = round(user_money, 2) // .01

    change_format = (
        "Your change is:\n"
        f"{int(dollars)} dollar{'s' if dollars > 1 or dollars == 0 else ''}\n"
        f"{int(quarters)} quarter{'s' if quarters > 1 or quarters == 0 else ''}\n"
        f"{int(dimes)} dime{'s' if dimes > 1 or dimes == 0 else ''}\n"
        f"{int(nickels)} nickel{'s' if nickels > 1 or nickels == 0 else ''}\n"
        f"{int(pennies)} {"pennies" if pennies > 1 or pennies == 0 else "penny"}\n"
    )

    print(change_format)

if __name__ == "__main__":
    print('*' * 33)
    print("Welcome to vending machine bravo!")
    print('*' * 33)
    money = money_input()
    item_price = item_selection(money)
    change_dispenser(money, item_price)

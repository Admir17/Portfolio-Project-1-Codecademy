MONEY = 50


def check_balance():
    print(f"You have ${MONEY} left.\n")
    return MONEY


def program_start():
    print("\n---Welcome to New York Subway!---\n")
    print("What kind of Ticket are you interested in?")
    print("""
        1. Single Ride Ticket
        2. 7-Day Unlimited Ticket
        3. 30-Day Unlimited Ticket\n""")

    while True:
        num = int(input("Enter a number: "))
        if num not in [1, 2, 3]:
            print("Invalid Input, try again")
        else:
            break

    match num:
        case 1:
            print("Here is the price information: A Single Ride Ticket costs $2.90")
            price = 2.90
        case 2:
            print("Here is the price information: A 7-Day Unlimited Ticket costs $34")
            price = 34
        case 3:
            print("Here is the price information: A 30-Day Unlimited Ticket costs $132")
            price = 132

    print("Would you like to continue and buy a ticket?")

    while True:
        answer = input("Yes/No: ")
        if answer.lower() not in ["yes", "no"]:
            print("Invalid Input, try again")
        else:
            break

    match answer.lower():
        case "yes":
            print("Checking balance...")
            balance = check_balance()
            if balance >= price:
                print("Purchase succeded, here is your Ticket! Goodbye!")
            else:
                print("You do not have sufficient money, come around next time!")
        case "no":
            print("Goodbye!")


def main():
    program_start()


main()

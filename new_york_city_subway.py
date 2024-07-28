MONEY = 150


def check_balance():
    print(f"You have ${money} left.")


def program_start():
    print("\n---Welcome to New York Subway!---\n")
    print("What kind of Ticket are you interested in?")
    print("""
        1. Single Ride Ticket
        2. 7-Day Unlimited Ticket
        3. 30-Day Unlimited Ticket\n""")

    answer = input("Enter a number: ")
    match answer:
        case '1':
            print("A Single Ride Ticket costs $2.90")
        case '2':
            print("A 7-Day Unlimited Ticket costs $34")
        case '3':
            print("A 30-Day Unlimited Ticket costs $132")
        case _:
            print("Invalid Input")


def main():
    program_start()

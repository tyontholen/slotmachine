MAX_LINES = 3


def deposit():
    while True:
        ammount = input("How much do you want to deposit? $$$ ")
        if ammount.isdigit():
            ammount = int(ammount)
            if ammount > 0:
                break
            else:
                print("Ammount must be greater than 0 $$$")
        else:
            print("Please enter a number.")

    return ammount

# re-used code
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}) ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def main():
    balance = deposit()  
    lines = get_number_of_lines()

main()                             
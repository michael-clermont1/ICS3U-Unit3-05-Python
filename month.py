#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program shows formatting output


def main():
    # this function shows formatting output

    # input
    number = int(input("Enter the number of a month (ex: 1 for January): "))

    # process & output
    print("")
    if number == 1:
        print("The month is January.")
    elif number == 2:
        print("The month is February.")
    elif number == 3:
        print("The month is March.")
    elif number == 4:
        print("The month is April.")
    elif number == 5:
        print("The month is May.")
    elif number == 6:
        print("The month is June.")
    elif number == 7:
        print("The month is July.")
    elif number == 8:
        print("The month is August.")
    elif number == 9:
        print("The month is September.")
    elif number == 10:
        print("The month is October.")
    elif number == 11:
        print("The month is November.")
    elif number == 12:
        print("The month is December.")
    else:
        print("That is not a month!")

    print("\nDone.")


if __name__ == "__main__":
    main()

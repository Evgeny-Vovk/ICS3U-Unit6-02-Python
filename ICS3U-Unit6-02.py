# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: January 2023
# ICS3U-Unit6-02.py File, learning functions with parameters in python.

import random


def largest_number(random_numbers):
    answer = 0
    for counter in range(len(random_numbers)):
        if answer < random_numbers[counter]:
            answer = random_numbers[counter]
    return answer


def main():

    random_numbers = []

    for counter in range(10):
        number = random.randint(0, 100)
        random_numbers.append(number)
        print("Generated number: {0}".format(number))

    answer = largest_number(random_numbers)

    print("\nThe largest number of all numbers is {0}.".format(answer))
    print("")

    print("\n\nDone.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Function to check if a number
# is a Curzon number or not
def checkIfCurzonNumber(N):
    powerTerm, productTerm = 0, 0

    # Find 2^N + 1
    powerTerm = pow(2, N) + 1

    # Find 2*N + 1
    productTerm = 2 * N + 1

    # Check for divisibility
    if (powerTerm % productTerm == 0):
        print(f"N 是 curzon 数")
    else:
        print("N 不是 curzon 数")


if __name__ == '__main__':
    number = int(input("Write a number "))
    checkIfCurzonNumber(number)




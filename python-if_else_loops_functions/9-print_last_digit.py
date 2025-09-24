#!/usr/bin/python3

def print_last_digit(number):

    if number < 0:
        last_digit = -(-number % 10)
    else:
        last_digit = number % 10

    print(last_digit)
    return last_digit

r = print_last_digit(21)   # imprime 1, r recebe 1
r = print_last_digit(-21)  # imprime 1, r recebe 1

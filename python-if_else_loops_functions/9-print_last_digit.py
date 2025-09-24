#!/usr/bin/python3

def print_last_digit(number):

    last_digit = abs(number) % 10  # pega o valor absoluto antes de % 10

    print(last_digit)
    return last_digit

r = print_last_digit(21)   # imprime 1, r recebe 1
r = print_last_digit(-21)  # imprime 1, r recebe 1

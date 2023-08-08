#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit
uppercase = __import__('8-uppercase').uppercase
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")

uppercase("best")
uppercase("Best School 98 Battery street")
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

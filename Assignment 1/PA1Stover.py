''' Assignment: Fractions

   PA1Stover.py

   Name: Tayven Stover 

   File Created on February 7, 2024   

'''
"""
    Inputs:
        numerator
        denominator

    Outputs:
        is the fraction proper or improper
        proper fraction
        a / x is an improper fraction and its mixed fraction is y + z / l. ----improper
        a / x is a proper fraction. ----proper

    Take two integers, numerator and denominator

    Issue test case:
    -9 / 7 is a an improper fraction and its mixed fraction is -(1 + 2 / 7).

"""

input_numerator = int(input("Enter a numerator: "))
input_denominator = int(input("Enter a denominator: "))

def check_fraction(input_numerator, input_denominator):
    if input_numerator < input_denominator and input_numerator > 0:
        print(f"{input_numerator} / {input_denominator} is a proper fraction.")

    elif input_numerator < 0 and input_denominator > 0:
        proper_whole = int(input_numerator / input_denominator)
        proper_numerator = abs(input_numerator) % input_denominator

        if proper_numerator == 0:
            print(f"{input_numerator} / {input_denominator} is an improper fraction and it can be reduced to {proper_whole}")
        else:
            print(f"{input_numerator} / {input_denominator} is an improper fraction and its mixed fraction is -({abs(proper_whole)} + {proper_numerator} / {input_denominator})")

    elif input_numerator < 0 and input_denominator < 0:
        numerator = abs(input_numerator)
        denominator = abs(input_denominator)
        check_fraction(numerator, denominator)

    else:
        proper_whole = int(input_numerator / input_denominator)
        proper_numerator = input_numerator % input_denominator

        if proper_numerator == 0:
            print(f"{input_numerator} / {input_denominator} is an improper fraction and it can be reduced to {proper_whole}")
        else:
            print(f"{input_numerator} / {input_denominator} is an improper fraction and its mixed fraction is {proper_whole} + {proper_numerator} / {input_denominator}")
    
check_fraction(input_numerator, input_denominator)
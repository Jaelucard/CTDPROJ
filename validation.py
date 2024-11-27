#------------------------------------Validation Functions------------------------------------#
from math import gcd
# Function to validate integer input
class Validation:
    def get_integer_input(prompt, variable):
        while True:
            try:
                value = int(input(prompt).replace(" ", ""))  #check if input is an integer
                if variable == 'm':
                    if gcd(value, 26) == 1:  #check if the value is coprime with 26
                        return value
                    else:
                        print("Invalid value. Please choose a value (or its negative) that is coprime with 26 (i.e., its greatest common divisor with 26 is 1).\n")
                else:
                    return value
            except ValueError:  # If conversion fails, prompt again
                print("The value has to be an integer, please input a new value.\n")
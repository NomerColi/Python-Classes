"""
Example for using the Python random module.

Please visit the link below for the reference documentation to the random module.
https://docs.python.org/3/library/random.html#functions-for-integers
"""

# when using a module, make sure to import it first
import random

for x in range(0, 10):
    # random.randint(a, b) randomly generates an integer i such that a <= i <= b
    random_integer = random.randint(5, 30)
    print('Generated the integer', random_integer)

"""
The above code generates output resembling the following:

Generated the integer 28
Generated the integer 19
Generated the integer 26
Generated the integer 24
Generated the integer 30
Generated the integer 14
Generated the integer 25
Generated the integer 11
Generated the integer 26
Generated the integer 27
"""
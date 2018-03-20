# Modify print_time to make it a decorator that prints the time a certain function
# takes to execute
# NOTE THAT WE USE FLOATS FOR THE SECONDS
# MAKE SURE YOU USE THE FORMAT USED BELOW
# HINT: TRY USING TIME

import time

def print_time():
    print(0.0)

# Set print_time as a decorator of my_slow_operation, don't modify
# the implementation of the function.
def my_slow_operation(seconds_to_sleep):
    time.sleep(seconds_to_sleep)

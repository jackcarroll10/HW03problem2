import random

def max_value():
    value_1 = random.randint(0, 100)
    value_2 = random.randint(0, 100)
    if value_1 > value_2:
        print(value_1)
    if value_2 > value_1:
        print(value_2)
    if value_1 == value_2:
        print(value_1)

max_value()
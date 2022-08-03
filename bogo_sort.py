import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])
# print(numbers)

def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    with open('./numbers/1000_numbers.txt', 'w') as f:
        for i in range(len(values) - 1):
            f.write('%d' % values[i] + "\n")
            return values 

print(bogo_sort(numbers))   
# Graham Joonsar
# Can find the factors of any positive or negative integer

import time

start_time = time.time()

def findFactors(num):
    old_num = num  # This is used to tell if the num is negative
    num = abs(num)  # This makes sure that the number is positive
    factors = [(1, num)]  # One and the number will always be factors
    factors_already = []  # this helps make sure there are no duplicate factor pairs
    if num % 2 == 0: # Checks if the number is even
        for i in range(2, int(num / 2)):  # Only half the numbers need to be checked
            if num % i == 0:
                if i not in factors_already:
                    factors_already.append(num / i)
                    factors.append((i, num / i))
    elif num % 2 == 1: # checks if it is odd
        for j in range(3, int(num / 2 - 0.5), 2):  # Skips all even numbers; Odd numbers cant be divided by even numbers
            if num % j == 0:
                if j not in factors_already:
                    factors_already.append(num / j)
                    factors.append((j, num / j))
    if old_num < 0:  # This is for negative number
        for pair in factors:
            pair[1] *= -1  # Only one number needs to be negative
    print(factors)


findFactors(3603600) # Highly composite number

print("\nTime taken for execution was " + str(time.time() - start_time))

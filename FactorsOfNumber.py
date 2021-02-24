# Graham Joonsar
# Can find the factors of any positive or negative integer

def findFactors(num):
    oldNum = num  # This is used to tell if the num is negative
    num = abs(num)  # This makes sure that the number is positive
    factors = [[1, num]]  # One and the number will always be factors
    factorsAlready = []  # this helps make sure there are no duplicate factor pairs
    if num % 2 == 0:
        for i in range(2, int(num / 2)):  # Only half he numbers need to be checked
            if num % i == 0:
                if i not in factorsAlready:
                    factorsAlready.append(num / i)
                    factors.append([i, num / i])
    elif num % 2 != 0:
        for j in range(3, int(num / 2 - 0.5)):
            if num % j == 0:
                if j not in factorsAlready:
                    factorsAlready.append(num / j)
                    factors.append([j, num / j])
    if oldNum < 0:  # This is for negative number
        for pair in factors:
            pair[1] *= -1  # Only one number needs to be negative
    print(factors)


findFactors(-100)
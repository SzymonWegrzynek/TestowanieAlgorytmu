import math


def primeFactors(n):
    factors = []

    if n <= 1:
        return

    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors


def inputLine():
    n = int(input("Enter an integer: "))
    result = primeFactors(n)


def printResult():
    if result:
        for factor in result:
            print(factor)


def main():
    n = inputLine()
    result = primeFactors(n)
    printResult(result)


main()

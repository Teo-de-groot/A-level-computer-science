import math
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
primes = [number for number in numbers if number > 1 for i in range(2, int(math.sqrt(number)) + 1) if number % i != 0]
print(primes)


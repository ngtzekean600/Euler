import math

def isPrime(number):
    if number%2 == 0:
        return False 
    if number %3 == 0:
        return False
    else:
        current = 5
        while current<= math.sqrt(number):
            if number%current == 0:
                return False
            current += 2
    return True

primeList=[2,3,5]
currentPrime = 5
count = 3
while count!= 10001:
    currentPrime += 2
    if isPrime(currentPrime):
        primeList.append(currentPrime)
        count += 1
print(primeList[-1])
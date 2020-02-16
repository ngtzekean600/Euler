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

primeList = [2,3,5]
current = 7
while current<2000000:
    if isPrime(current):
        primeList.append(current)
    current += 2
sum = 0
for i in primeList:
    sum += i
print(sum)


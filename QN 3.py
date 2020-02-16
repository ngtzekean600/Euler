import math

number = int(input('What is your number: '))
# We will check if there is any prime factor 2
if number % 2 == 0:
    while number % 2 == 0:
        number = number/2
    lastFactor = 2
else:
    lastFactor = 1
currentFactor = 3
while number > 1 and currentFactor <= math.sqrt(number):
    while number % currentFactor == 0:
        number = number/currentFactor
    lastFactor = currentFactor
    currentFactor = currentFactor + 2
if number == 1:
    print(lastFactor)
else:
    print(number)

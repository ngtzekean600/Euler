def isprime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
div = []
for i in range(1,600851475143+1):
    if 600851475143%i == 0:
        div.append(i)
        print(i)
        
primes = []
for i in div:
    if isprime(i)==True:
        primes.append(i)
prime.max()


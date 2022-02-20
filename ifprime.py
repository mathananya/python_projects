
def isprime(n):
    n = int(n)
    m = int(n**0.5)
    if n < 2:
        return False
    for div in range(2,m+1):
        if n%div == 0:
            return False
    return True

oldPrime = -5
for x in range(2,1000):
    if isprime(x):
        if x-oldPrime == 2:
            print(oldPrime," and ",x," are TWIN PRIMES\n")
        oldPrime = x

##oldPrime = 2
##newPrime = 2
##for x in range(1000001,1010000,2):
##    if isprime(x):
##        oldPrime = newPrime
##        newPrime = x
##        if newPrime-oldPrime == 2:
##            print(oldPrime," and ",newPrime," are TWIN PRIMES\n")

"""A collection of functions to generate lists of numbers, usually up to a maximum value n."""
import math

def gen_primes(n: int) -> list:
    """Generate all the prime numbers not greater than n using the Sieve of Eratosthenes."""
    prime = [True for p in range(n+1)]

    for i in range(2, int(math.sqrt(n)+1)):
        if prime[i] == True:
            for j in range(i**2, n+1, i):
                prime[j] = False
    
    primes = []
    for k in range(2, len(prime)):
        if prime[k] == True:
            primes.append(k)

    return primes

def gen_fibonacci(n: int) -> list:
    """Generate all the fibonacci numbers less than or equal to n."""
    fibs = [1,1]

    i = 2
    while fibs[i-1] + fibs[i-2] <= n:
        fibs.append(fibs[i-1]+fibs[i-2])
        i += 1
    return fibs
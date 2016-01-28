# Python 3.4 - Sieve of Eratosthenes
def gen_primes(limit):
    primes = []
    
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
           primes.append(num)
           for i in range(num * num, limit + 1, num):
               sieve[i] = False
    
    print(primes)
gen_primes(100) # Find primes within the limit of X.

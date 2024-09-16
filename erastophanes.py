import time
import timeit
import numpy as np
import numba as nb
@nb.jit(nopython=True)
def sieve_of_eratosthenes(limit):
    primes = np.ones(limit + 1, dtype=np.bool_)
    primes[:2] = False  # 0 and 1 are not prime numbers
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            primes[p*p:limit+1:p] = False

    prime_count = np.count_nonzero(primes)
    return prime_count

if __name__ == "__main__":
    limit = float(input("Enter the limit: "))
    limit = int(limit)
    sieve_of_eratosthenes(5)
    start_time = timeit.default_timer()
    prime_numbers = sieve_of_eratosthenes(limit)
    end_time = timeit.default_timer()

    print(f"Execution time: {end_time - start_time} seconds")
    print(f"Prime numbers up to {limit:,} are: {prime_numbers}")
    

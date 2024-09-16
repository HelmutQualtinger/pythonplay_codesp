import numba as nb
import time
import numpy as np

@nb.njit
def count_primes(limit):
    # Create a boolean array "is_prime[0..limit]" and initialize
    # all entries it as true.
    is_prime = np.ones(limit + 1, dtype=np.bool_)
    is_prime[0] = is_prime[1] = False

    # Use the Sieve of Eratosthenes algorithm to mark non-prime numbers.
    ll = int(limit ** 0.5) + 1
    for i in range(2, ll):
        if is_prime[i]:
            is_prime[i * i : limit + 1 : i] = False

    # Count the number of prime numbers.
    count = np.sum(is_prime)

    return count
start_time = time.time()
count_primes(1)
print (f"Warm-up:{time.time()-start_time}")

start_time = time.time()
count_primes_nb = count_primes(4_000_000_000)
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")
print(f"Number of primes found: {count_primes_nb}")



def count_primes(limit):
    # Create a boolean array "is_prime[0..limit]" and initialize
    # all entries it as true.
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    # Use the Sieve of Eratosthenes algorithm to mark non-prime numbers.
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Count the number of prime numbers.
    count = sum(is_prime)

    return count

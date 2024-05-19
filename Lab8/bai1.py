def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    primes = []
    for i in range(2, limit):
        if is_prime(i) and is_prime(i+2):
            primes.append((i, i+2))
    return primes

twin_primes = find_twin_primes(1000)
for pair in twin_primes:
    print(f"({pair[0]}, {pair[1]})")
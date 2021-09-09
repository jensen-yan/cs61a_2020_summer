def is_prime(x):
    if x <= 1:
        return False
    return all(map(lambda y: x%y, range(2,x)))

def sum_primes(a, b):
    return sum(filter(is_prime, range(a, b)))
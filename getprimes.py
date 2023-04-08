def sieve(limit: int) -> list:
    sieve: list = [False] * (10000000)
    sqrt_limit: int = int(limit ** 0.5) + 1

    primes: list = []
    for x in range(1, sqrt_limit):
            for y in range(1, sqrt_limit):
                    n: int = 4 * x ** 2 + y ** 2
                    if n <= limit and (n % 12 == 1 or n % 12 == 5):
                        sieve[n] = not sieve[n]
            
                    n = 3 * x ** 2 + y ** 2
                    if n <= limit and n % 12 == 7:
                        sieve[n] = not sieve[n]

                    n = 3 * x ** 2 - y ** 2
                    if x > y and n <= limit and n % 12 == 11:
                        sieve[n] = not sieve[n]
    primes = [2, 3]
    for n in range(5, limit + 1):
        if sieve[n]:
            primes.append(n)
    return primes



def sieve_iter():
    """
    This is an iterator that returns prime numbers.
    This does not use the "Sieve of Atkin".
    However, it will reach good performance
    """
    yield 2
    yield 3
    sieve = {}
    n = 5
    while True:
        if n not in sieve:
            yield n
            sieve[n * n] = [n]
        else:
            primes = sieve.pop(n)
            for prime in primes:
                sieve.setdefault(n + prime, []).append(prime)
        n += 2





if __name__ == "__main__":
    sieve(1000000, "test1")


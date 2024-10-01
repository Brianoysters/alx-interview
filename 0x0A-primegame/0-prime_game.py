#!/usr/bin/python3

def eratosthenes_sieves(n):
    """
    Generates a list of primes up to n using the Sieve of Eratosthenes
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False
    primes = [i for i in range(n + 1) if sieve[i]]
    return primes

def isWinner(x, nums):
    """
    Determines the winner after x rounds of prime game
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    primes = eratosthenes_sieves(max_num)

    win_count = {"Maria": 0, "Ben": 0}

    for n in nums:

        prime_count = len([p for p in primes if p <= n])

        if prime_count % 2 == 0:
            win_count["Ben"] += 1
        else:
            win_count["Maria"] += 1

    if win_count["Maria"] > win_count["Ben"]:
        return "Maria"
    elif win_count["Ben"] > win_count["Maria"]:
        return "Ben"
    else:
        return None


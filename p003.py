"""Problem 003

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def prime_factors(n):
    d = 2
    while n > 1:
        while n % d == 0:
            yield d
            n /= d
        d = d + 1

ans = max(n for n in prime_factors(600851475143))

print(ans)

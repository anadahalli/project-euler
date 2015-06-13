"""Problem 007

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import sqrt

is_prime = lambda n: not any([n % i == 0 for i in range(2, int(sqrt(n))+1)])


def nth_prime(n):
    count = 0
    prime = 2
    while True:
        if is_prime(prime):
            count += 1
        if count == n:
            return prime
        prime += 1

ans = nth_prime(10001)

print(ans)

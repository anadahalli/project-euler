"""Problem 010

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt

ans = sum(n for n in range(2, 2000000+1)
          if not any(n % i == 0 for i in range(2, int(sqrt(n))+1)))

print(ans)

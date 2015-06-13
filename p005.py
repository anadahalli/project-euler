"""Problem 005

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

from fractions import gcd
from functools import reduce

ans = reduce(lambda x, y: x * y // gcd(x, y), range(1, 20+1))

print(ans)

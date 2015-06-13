"""Problem 009

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

a, b, c = next((a, b, c)
               for a in range(1, 500)
               for b in range(1, 500)
               for c in range(1, 500)
               if a < b < c and a**2 + b**2 == c**2 and a + b + c == 1000)

ans = a * b * c

print(ans)

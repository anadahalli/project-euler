"""Problem 004

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

ans = max(a * b for a in range(1, 1000) for b in range(1, 1000)
          if str(a * b) == str(a * b)[::-1])

print(ans)

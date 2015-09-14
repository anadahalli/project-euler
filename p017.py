"""Problem 017

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

import re

unit_names = ('zero one two three four five six seven eight nine ten '
              'eleven twelve thirteen fourteen fifteen sixteen seventeen '
              'eighteen nineteen'
              ).split()
tens_names = ('zero ten twenty thirty forty fifty sixty seventy '
              'eighty ninety'
              ).split()


def english(n):
    """Return the English name for n, from 0 to 999999"""
    if n >= 1000:
        thous = english(n // 1000) + " thousand"
        n = n % 1000
        if n == 0:
            return thous
        elif n < 100:
            return thous + " and " + english(n)
        else:
            return thous + ", " + english(n)
    elif n >= 100:
        huns = unit_names[n // 100] + " hundred"
        n = n % 100
        if n == 0:
            return huns
        else:
            return huns + " and " + english(n)
    elif n >= 20:
        tens = tens_names[n // 10]
        n = n % 10
        if n == 0:
            return tens
        else:
            return tens + "-" + english(n)
    else:
        return unit_names[n]


def letter_count(s):
    """Return the number of letters in the string s"""
    return len(re.findall(r'[a-zA-Z]', s))

ans = sum(letter_count(english(i)) for i in range(1, 1001))

print(ans)

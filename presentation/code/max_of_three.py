# @Input1: an integer
# @Input2: an integer
# @Input3: an integer
# @Output: maximum among @Input1, @Input2 and @Input3
import ipdb

def maxOfThree(a, b, c):
    ipdb.set_trace()
    if a > b:
        if a > c:
            return a
        return b
    if b > c:
        return b
    return c

print maxOfThree(5, 2, 7)
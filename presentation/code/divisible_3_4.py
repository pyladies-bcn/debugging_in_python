# @Output: a sorted list of all non-negative numbers less than
# 30 which are divisible both by 3 and by 4
import ipdb

def threeAndFour():
    result = []
    for counter in range(30):
        if counter % 3 == 0 or counter % 4 == 0:
            ipdb.set_trace()
            result.append(counter)
    return result

print threeAndFour()
# @Output: a sorted list of all non-negative numbers less than
# 30 which are divisible both by 3 and by 4
import ipdb

def function2(param_a, param_b):
    if param_a > param_b:
        return param_a
    else:
        return param_b

def function(param_a, param_b):
    ipdb.set_trace()
    return function2(param_a, param_b)

print function(7, 5)
import math

def distance(a, b):
    if (a == b):
        return 0
    elif (a < 0) and (b < 0) or (a > 0) and (b > 0):
        if (a < b):
            return (abs(abs(a) - abs(b)))
        else:
            return -(abs(abs(a) - abs(b)))
    else:
        return math.copysign((abs(a) + abs(b)),b)

print(distance(123, 321))

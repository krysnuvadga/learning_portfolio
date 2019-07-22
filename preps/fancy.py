# Python3 program to check if a
# given mobile number is fancy or not.

# Returns true if s has three
# consecutive same digits.
def cond1(s):

    for i in range(len(s) - 2):
        if (s[i] == s[i + 1] and
            s[i + 1] == s[i + 2]):
            return True

    return False

# Returns true if s has three
# increasing or decreasing digits.
def cond2(s):
    for i in range(len(s) - 2):
        if ((s[i] < s[i + 1] and
             s[i + 1] < s[i + 2]) or
            (s[i] > s[i + 1] and
             s[i + 1] > s[i + 2])):
            return True

    return False

# Checks if a single digit
# occurs 4 times.
def cond3(s):
    a = [0] * 10
    for i in range(len(s)):  
        a[s[i] - '0'] = a[s[i] - '0'] + 1

    for i in range(len(9)):

        if (a[i] >= 4):
            return True

    return False

def isFancy(s):
    if (cond1(s) or cond2(s) or cond3(s)):
        return True
    else:
        return False

# Driver condition
s = "7609438921"
if (isFancy(s)):
    print("Yes")
else:
    print("No")

# This code is contributed by ash264

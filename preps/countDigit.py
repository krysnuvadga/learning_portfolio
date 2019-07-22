# Recursive Python program to count
# number of digits in a number

def countDigit(n):
    if n == 0:
        return 0
    return 1 + countDigit(n // 10) 

# Function to check whether the given number is
# Armstrong number or not
def isArmstrong (x):
    n = order(x)
    temp = x
    sum1 = 0
    while (temp!=0):
        r = temp%10
        sum1 = sum1 + power(r, n)
        temp = temp/10

    # If condition satisfies
    return (sum1 == x) 

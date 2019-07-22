def reverse(number):
    rev = 0
    while number > 0:
        reminder = number % 10
        rev = (rev*10) + reminder
        number = number//10
    return rev

print(reverse(123))

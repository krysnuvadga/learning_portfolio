def fizzbuzz(numbers):
    for i, num in enumerate(numbers):
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = 'fizzbuzz'
        elif num % 3 == 0:
            numbers[i] = 'fizz'
        elif num % 5 == 0:
            numbers[i] = 'buzz'
    print(numbers)
numbers = [45, 22, 14, 65, 97, 72] 

print(fizzbuzz(numbers))
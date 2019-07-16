import random

# function to read a random line from a file.
def method1(fname):
    count = open(fname).read().splitlines()
    return random.choice(count)

# to count the number of lines in a text file
def method2(fname):
    with open(fname) as f:

        for i, l in enumerate(f):
            pass
    return i + 1

# function to calculate the sum of a list of numbers.
def list_sum(list):
    sum = 0

    for number in list:
        sum += number
    return sum


# function that checks whether a passed string is palindrome Or not
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1

	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True

# Alternatively
def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


# Function that accepts a string and calculate the number of upper case letters and lower case letters
def lowerUpper(string):
    d = {"UPPER_CASE":0, "LOWER_CASE":0}
    for c in string:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("Number of upper case characters:", d["UPPER_CASE"])

    print("Number of lower case characters:", d["LOWER_CASE"])

# Program to remove vowels from a String
def rem_vowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for char in string.lower():
        if char in vowel:
            string = string.replace(char, " ")
            
    print(string)


#Function to reverse a given string
def string_reversal(s):
    output = s[::-1]
    print(output)

def reversal():
    s = input("Enter some string:" )
    output = " "
    i = len(s)-1
    while i >= 0:
        output = output+s[i]
        i=i-1
    print(output)
# this is a comment
"""Welcome to Python """  # also a comment

""" Data Types """
# All variables start with a lowercase by default

name = 'Jaxon'
age = 5
is_old = False  # Boolean
sei_1019 = True  # True/False must be capitalized

print(name)  # same as console.log()
# run python3 filename to print in terminal

# Runs line by line so both names will print
name = 'Rome'
print(name)

""" Methods for a string """

sentence = 'Today is Nicoles birthday'

# splits each word in sentence
nicole_birthday = sentence.split(' ')
print(nicole_birthday)

# Joins words back together
new_sentence = " ".join(nicole_birthday)
print(new_sentence)

# gets index of letter
print(new_sentence.index('N'))

# Upper and lower case
name.upper()
name.lower()

# replace
day_sentence = sentence.replace('birthday', 'Day')
print(day_sentence)

# in keyword
is_day = 'Day' in day_sentence  # returns boolean
print(is_day)

day_sentence

# ranges

# str[index] choose one letter at index
# str[-index] choose letter at index counting backwards from the end.
# str[start:end] get a range of letters from a start to end.
# str[start:end:step] get a range of letters taking step sized steps between.
# str[:end] omit the start index and grab letters from zero up to end.
# str[start:] omit the end index and grab letters from start up to the end of the string.
# str[::-1] reverses a string by going backwards with a step of -1 from start to end.

day_sentence[-1]  # returns last letter

nicole_range = day_sentence[9:15]  # returns a range of letters (Nicole)
print(nicole_range)

# length
print(len(nicole_range))  # returns length of string

# logical operators

equal_to = 5 == 5  # Returns boolean (True), checks for data type
not_equal = 5 != 5  # Returns boolean (False)

not True  # returns false
not False  # returns true

true_story = 5 <= 5
this_should_be_true = 6 >= 5

print(9 < 30)  # returns boolean (True)

print(5 < 4 or 6 > 30)  # returns False and uses or instead of ||

print('Rome' == 'rome' or 'Pete' == 'Pete')  # returns True
# uses and instead of && and returns False
print('Rome' == 'rome' and 'Pete' == 'pete')

print('' or 'Rome')  # prints the truthy value (Rome)
print(0 or 5)  # prints the truth value (5)

print(5 < age < 6)  # returns False

real_name = name or False  # select name first because False is a falsey value

# lists
# lists are the same thing as arrays

numbers = [3, 4, 5, 6]
print(len(numbers))  # returns length of list

numbers[1]  # returns index number 0

print(numbers[-1])  # returns last number in list

print(numbers[len(numbers) - 1 * 2])  # returns the number 5

five_rome = ['Rome'] * 5  # returns Rome 5 times
print(five_rome)

# itterate through a list of numbers
one_through_five = list(range(5))  # returns list of numbers 1-5
print(one_through_five)

for i in range(len(one_through_five)):  # : is the same as {}
    num = one_through_five[i]
    print(num)  # prints each number in the list seperately

# itterate through a list
orcas = ['Jaxon', 'Simone', 'Nicole', 'Edrees']

# must indent properly for code to work
for i in range(len(orcas)):
    orca = orcas[i]
    print(orca)  # prints each name in the list seperately

random_numbers = [45, 88, 4, 17]
random_numbers.sort()  # sorts numbers in order from smallest to largest
print(random_numbers)

# sorted_numbers = random_numbers.sort()
# print(sorted_numbers)

# not sorted anymore since it was appended after the sort
random_numbers.append(33)  # adds number to the end of the string
print(random_numbers)

reverse_random_numbers = random_numbers[::-1]  # reverses the order of numbers
print(reverse_random_numbers)

thirty_three = random_numbers.pop()  # removes the last number from the list (33)
print(thirty_three)

random_numbers.insert(1, 99)  # puts 99 in the second index
print(random_numbers)

print(random_numbers.count(45))  # shows how many times 45 occured in the list

# help
# shows all built in methods for list and what those methods do and what error will come up if there is something wrong
# print(help(random_numbers))

# Dictionaries
# objects are call dictionaries in python
car = {
    # key and value must be in a string
    "color": "red",
    "make": "Tesla",
    "model": "S",
    "all_colors": ['red', 'white', 'black'],
    "cool_car": True,
    "other_tesla_products": {
        "prodcut": "Model 3",
        "product2": "Model X",
        "product3": "Cybertruck"
    }
}
print(car["make"])  # returns "Tesla"

# print(help(car)) :wq to escape in terminal

car["speed"] = 200  # adds to car dictionary
print(car)

print(car.get("color"))  # returns red

print(car.items())  # returns all items

print(car.keys())  # returns all keys

# type convention

int('33')  # changes to integer

str(33)  # changes to string

float(33)  # adds decimal

bool(0)  # returns False because its a falsey value
bool(3)  # returns True because its a truthy value

# string interpolation

print('Hello my name is ' + name)  # both do the same thing
print(f'Hello my name is {name}')  # both do the same thing

phrase = 'This {} is a phrase {}'
# puts 'sentence' and name inside of the brackets
phrase.format('sentence', name)  # doesnt actually change phrase

# functions


def print_name(someone):
    return someone


print(print_name('Nicole'))


def old_enough(age):
    if age < 21:
        return 'Not old enough'
    elif age == 21:  # same as else if
        return 'You made it to adulthood'
    else:
        return 'Toure older, nice'


print(old_enough(21))
print(old_enough(20))
print(old_enough(22))


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def random_function(num1, num2, num3):
    return num1 * num2 - num3


print(add(1, 1))
print(subtract(2, 1))
print(random_function(4, 6, 8))

# getting input from the user

age = input('How old are you? ')
print(age)

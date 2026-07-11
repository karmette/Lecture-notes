####################################################
# Loop Controls                                    #
####################################################

# TODO: Make a for loop that terminates when it encounters a negative number.

# numbers = [12, 8, 3, -4, 9, 15]

# for number in numbers:

#     if number < 0:
#         break

#     print(number)

# TODO: Write a while loop that accepts the user's name as input and terminates when they say to quit.

# while True:
#     name = input("Enter your name (or 'quit'): ")

#     if name.lower() == "quit":
#         break

#     print("Hello", name)

# TODO: Write a for loop that prints only the even numbers from 1-20.
# for number in range(1, 21):

#     if number % 2 != 0:
#         continue

#     print(number)

# TODO: Write a for loop that skips the "O" in the word "PYTHON" and prints all the other letters.
# word = "PYTHON"

# for letter in word:

#     if letter == "O":
#         continue

#     print(letter)

# TODO: Write a for loop that prints numbers from 0-4 and uses the pass keyword if the number = 3.
# for number in range(5):

#     if number == 3:
#         pass

#     print(number)

####################################################
# For Loops - Range                                        #
####################################################

# TODO: Write a for loop that prints every other number from 2-10 (inclusive)

# for i in range(2, 11, 2):
#     print(i)

# TODO: Write a for loop that prints every third number from 15-0 (inclusive)
# for i in range(15, -1, -3):
#     print(i)

# TODO: Write a for loop that checks a range of 100 numbers and prints only even numbers < 20
# Work with a partner :) Hint, use the continue and break keywords to accomplish this

# for i in range(0,100):
#     if i % 2 == 1: #if the number is odd skip it
#         continue
#     if i >= 20: #if the number >= 20, terminate
#         break

#     print(i)

####################################################
# Looping Through Strings                          #
####################################################

# TODO: Write a for loop that checks each character in the message variable provided and 
# replaces all the special characters with a space

message = "Welcome@to#Python!Programming$101"

clean_message = ""

# for letter in message:

#     if letter in "@#!$":
#         clean_message += " "
#     else:
#         clean_message += letter

# print(clean_message)

####################################################
# Functions                                        #
####################################################

## Key Concepts:
# - def keyword
# - Parameters and arguments
# - Return values
# - Default arguments

## Code Demo:
# def greet(name="world"):
#     return f"Hello, {name}!"
# print(greet("Alice"))
# print(greet())


# def test_function():
#     print("Hello, World!")

# test_function()


# def another_function():
#     for i in range(10):
#         print(i)

# another_function()

# def say_hello(greeting):
#     print(greeting)

# say_hello("Hello!")

# def greet_many_times(greeting, number_times):
#     return 10


# number = greet_many_times("Hello!", 1000)

# print(number)

# len(list)


## Exercises:
# Write a function that returns the square of a number.


# def stop_at_five(count):
#     for num in range (count):
#         if num == 5:
#             return 5
#         else:
#             print(num)

        # print("Got to the end")

# num = stop_at_five(10)

# print(num)


# Write a function that returns True if a number is even, False otherwise.



# for i in range(5):
#     num = int(input("Enter a number: "))

#     res = is_even(num)
#     if res == True:
#         print("The number you entered is even")
#     elif res == False:
#         print("The number you entered is odd")


# Write a function that takes in someone's first and last name as
# separate inputs and returns a string with the names combined
# def combine_name(first_name, last_name):
#     return first_name + " " + last_name

# first_name = "Sayid"
# last_name = "Hinds"

# print(combine_name(first_name, last_name), "is in the Python class")

# Write a function that returns either the minimum, maximum or the average of a list of numbers
# numberList = [2,5,9,13,15]


# print(numberStatistics(numberList, "max"))


####################################################
# Scope                                            #
####################################################

## Key Concepts:
# - Local vs global variables
# - Variable shadowing
# - Scope lifetime

## Code Demo:
# x = 10
# def change_x():
#     x = 5
#     print("Inside:", x)
# change_x()
# print("Outside:", x)

## Exercises:
# Predict output for different scope examples.

# x = "universe"
# print("Main sees:", x) 

# def outer():
#     def inner():
#         x = 5
#         print("Inner sees:", x)
#         def even_inner():
#             x = 5
#             print("Even Inner sees:", x)
#     print("Outer sees:", x) #2
#     inner()

# outer()
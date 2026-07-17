# Homework 3 
# Part 1: Functions & Exception Handling

# TODO: Create get_user_input(prompt) to safely take input such as a user's first name, last name and email address
# TODO: Add calculate_age_in_months(user) that returns age * 12
# Be sure to use exception handling in your function to catch any issues with user input

# Sample structure:
# def get_user_input(prompt):
#     try:
#         return input(prompt)
#     except:
#         return ""

# def view_profile(user):
#     print(user)

# Part 2: Classes

# TODO: Create a class called User and initialize:
# name, age, student, hobbies, location

# TODO: Add methods:
# view_profile(), add_hobby(), calculate_age_in_months()


# STARTER CODE

# class User:
#     def __init__()


"""
TODO: Using inheritance, create a subclass called Admin with
      a new password parameter and a method called login.
      Login should prompt the Admin for a password until
      either the user exits or gets the password right.
"""

import random

# Part 3: Modules
# TODO: Make a random password generator!
# Using the random library, make a function that generates a sequences of:
# Random letters: A-Z, a-z
# Random numbers: 0-9
# And random symbols: %$!@#
# Allow the user to specify the password length, and if they want special characters. (Your parameters)
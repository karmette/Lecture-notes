####################################################
# Error Handling                                   #
####################################################

# Debugging
## Description:
# Learn how to read error messages and use try/except.

## Key Concepts:
# - Common errors (NameError, TypeError)
# - try/except blocks
# - print-debugging

## Code Demo:
try:
    val = int(input("Enter number: "))
    print("Value is:", val)
except ValueError:
    print("Invalid input!")

## Exercises:
# Fix broken code snippets with bugs.
# Write a function that divides two numbers and handles division by zero and non number inputs.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Please enter numbers only"    

print(safe_divide(10, 0))

def abs(x):
    """ Assumes x is an int
    Returns x if x>=0 and –x otherwise """
    if x < -1:
        print(x)
        return -x
    else:
        print(x)
        return x

## Tips for coding: always try to debug before asking for help.

####################################################
# Classes                                          #
####################################################

## Key Concepts:
# - class and __init__
# - self keyword
# - instance variables and methods

"""
BASIC STRUCTURE:

class <class name>:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def method1(self):
        pass

"""
# my_list = [1,2,3]
# my_list.

# class My_House():
#     description = "Something you live in"  # class attribute

#     def __init__(self, no_windows, no_doors): # init for initalize
#         self.no_windows = no_windows  # instance attributes
#         self.no_doors = no_doors
#         pass

#     def print_no_windows(self, random_number):
#         print(f"The number of windows in my house is {self.no_windows * random_number}")

#     def add_more_windows(self, number_windows):
#         self.no_windows += number_windows

# house1 = My_House(no_windows=10, no_doors=20)  # An instance of the My_House class with variables windows = 10 and doors = 20

# house1.no_windows = 20
# del house1.description
# print(house1.description)

# house1.print_no_windows(1)
# house1.add_more_windows(10)
# house1.print_no_windows(1)

# My_House.print_no_windows(house1, 1)
# My_House.add_more_windows(house1, 10)


# house2 = My_House(20, 10)
# print(house2.description)
# print(house2.no_doors)



# print(house.description)
# house.explode()

# house.description = "fat"

# print(house.description)
# print(house2.description)


# Code Demo:
# class Dog:
#     breed = "Golden retriever"
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(f"{self.name} says woof!")

#     def rename(self, name):
#         self.name = name


# my_dog = Dog("Spot")
# my_dog.name = "Rio"

# print(my_dog.name)

# my_dog.bark()

# print(my_dog.bark())


# TODO: Create a student class. Storing a student's Name, Age, Grade, and Classes


class Student():
    def __init__(self, name, age, grade, classes):
        self.name = name
        self.age = age
        self.grade = grade
        self.classes = classes

    def print(self):
        print(f"{self.name} is {self.age} and {self.grade}th grade in {self.classes}")

student_1 = Student("Bob", 14, 7, ["Math", "Science", "English"])

# student_1.name
# student_1.print()

# my_dict = {
#     "fsd" : 234
# }

# my_dict["fsd"]

# Student.print(student_1)


# formatted_string = f"{15 + 5}  "

# class list(list):
#     pass

# my_list = list(range(5))
# # print(my_list)

# print(my_list.__dir__())

# my_list.name = "hi!"
# print(my_list.name)


####################################################
# Inheritance                                      #
####################################################

## Key Concepts:
# - Inheriting with `class SubClass(ParentClass):`
# - Overriding methods
# - super()

## Code Demo:

class Human:
    def speak(self):
        return "language"
    def describe(self):
        return "I am from earth."

class Barbados(Human):
    def speak(self):
        return "Bajan"
    def food(self):
        return "I love flying fish and cou-cou."

class Jamaica(Human):
    def speak(self):
        return "Jamaican"
    def food(self):
        return "I love jerk chicken and rice and peas."

# print(Jamaica().describe())


## Exercises:
# Create a `Vehicle` class and extend it into `Car` and `Bike`.
# Create a `Shape` class and inherit `Rectangle` and `Circle` with methods to compute area.

class Shape:
    def __init__(self, no_sides):
        self.no_sides = no_sides

class Rectangle(Shape):
    def __init__(self, no_sides, length, breadth):
        super().__init__(no_sides)
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"The area is {self.length * self.breadth}")

class Circle(Shape):
    def __init__(self, no_sides, radius):
        super().__init__(no_sides)
        self.radius = radius

    def area(self):
        print(f"The area is {(self.radius * 3.14) ** 2}")


Rectangle(4, 2, 6).area()

####################################################
# Modules                                          #
####################################################

# Section 4: Modules
## Description:
# Introduce importing and using Python’s standard library.

## Key Concepts:
# - import keyword
# - Using functions from modules
# - Popular modules: math, random, os

## Code Demo:
import random
print("Random number:", random.randint(1, 10))

## Exercises:
# Use math module to compute square root.
import math
print("Square root of 16:", math.sqrt(16))
# Use random module to build a simple dice roller.
def roll_dice():
    return random.randint(1, 6)

print("Dice roll:", roll_dice())

# TODO: Create a number guessing game, where the computer picks a number and the user guesses.
# The user can try again until they get it, and tell the user if they were too high or too low.
# Count the number of tries it took for the user to do it!


# TODO: Create a program that calculates four options:
# Area of circle (given radius)
# Circumference (given radius)
# Hypotenuse of right triangle (given length of two legs)
# Square root (given any integer)
# Create a function for every operation!


# TODO: Your turn!
# Create a program that picks a random integer between 1-20
# And use that number as the radius of a circle and calculate the area!
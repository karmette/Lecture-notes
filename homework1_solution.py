# Homework 1 Template: Getting Started with Your Assistant

# Part 1
# Create a file named assistant.py and use it to complete the following tasks
# TODO: Greet the user
# TODO: Ask for their name, age, and if they are a student
# TODO: Store the info in variables
# TODO: Use type() to check types
# TODO: Use int() to cast input as needed
# TODO: Print the value of the variables and their types

# Example:
# name = input("What is your name? ")

# Part 2
# TODO: Create a calculator capable of addition, subtraction, multiplication, division, and exponentiation
# TODO: Ask the user to input two numbers
# TODO: Ask the user to choose between the above choices
# TODO: Output the solution based on the user's choices
# TODO: Use int() to cast input to make numbers usable
# TODO: Use if statements to make sure the correct output is achieved

n1 = int(input("Type a number: "))
n2 = int(input("Type another number: "))
operation = input("Would you like to add, subtract, multiply, divide, or power? ")
if operation == "add":
    print(n1,"+",n2,"=",n1+n2)
elif operation == "power":
    print(n1,"^",n2,"=",n1**n2)


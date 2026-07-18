# ==========================================
# Topic: File I/O
# ==========================================
#
# Scenario:
# You own a Caribbean restaurant. Every time a customer places
# an order, you save it in a file.
#
# ----------------------------------------------------------------------------
# TODO: Add Orders to the file by asking customers for their name and order
# ---------------------------------------------------------------------------
#
# #
# customer_name = input("Enter customer name: ")
# order = input("Enter customer order: ")

# with open("orders.txt", "a") as file:
#     file.write(customer_name + ", " + order + "\n")

# print("Order saved!")

# ------------------------------------------
# TODO: Read the File and display the orders
# ------------------------------------------

# with open("orders.txt", "r") as file:
#     for order in file:
#         print(order.strip())

# ------------------------------------------
# TODO - Count the number of Orders
# ------------------------------------------
# #
# count = 0

# with open("orders.txt", "r") as file:
#     for order in file:
#         print(order.strip())
#         count += 1

# print("Total Orders:", count)

# -----------------------------------------------------------------------------
# TODO: What do you think will happen if we change append ('a') to write ('w')?
# -----------------------------------------------------------------------------

# customer_name = input("Enter customer name: ")
# order = input("Enter customer order: ")

# with open("orders.txt", "w") as file:
#     file.write(customer_name + ", " + order + "\n")

# print("Order saved!")


# More exercises! (Aaron)

# Searching through records
# Given a file with the format:
'''
1001,John Smith
1002,Alice Brown
1003,Michael Lee
'''
# Prompt a user for an ID, and return the name associated with that ID

def find_name(id):
    pass # Put your code here!

### Max, min, avg

# We covered this, but we'll do it again!
# Given a file of numbers, return the avg, max, and min

### Score report
# You're given an earnings report for a company.
'''
January,12500
February,9800
March,14300
April,11750
May,15600
June,13400
July,14950
August,12100
September,8900
October,16250
November,13800
'''
# You have to write the earnings report to a file "earnings_report.txt"!
# Give the best performing month, worst performing month, average earnings

### Appending to file!
# You may notice the file is missing december!
# Append the december earnings (15400)
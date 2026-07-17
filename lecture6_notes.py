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

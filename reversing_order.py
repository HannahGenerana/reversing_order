# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# pseudocode

# ask the user to input a integer
random_number = input("Kindly input any random number: ")

# create a function
def reverse_order (digits):

# string the parameter to reverse its order
    reverse_digits = str(digits[::-1])

# create a loop for spacing
    for i in reverse_digits:
        print (i, end=" ")

# print the reverse order of the integer
reverse_order(random_number)
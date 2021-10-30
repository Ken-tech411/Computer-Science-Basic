import math
from turtle import *
# Bai 1 
# number = int((input("Input number: ")))

# if (number % 2 != 0):
#     print(f"{number} is an odd number")
# else:
#     print(f"{number} is an even number")

# Bai 2
# num = float((input("Input number: ")))

# if (num % 1 != 0):
#     print(f"{num} is not an interger")
# else:
#     print(f"{num} is an interger")

# Bai 3   
# input = input("Input character: "))

# try:
#     input == int(input)
#     print(f"'{input}' is a digit")
# except:
#     print(f"'{input}' is not a digit")
# Bai 4 
# num = float((input("Input number: ")))
# condition3 = int(3)
# condition5 = int(5)

# if num % condition3 == 0 and num % condition5 == 0:
#     print(f"{num} is divisible by 3 and 5")
# elif num % condition3 != 0 and num % condition5 == 0:
#     print(f"{num} is divisible by 5")
# elif num % condition3 == 0 and num % condition5 != 0:
#     print(f"{num} is divisible by 3")
# elif num % condition3 != 0 and num % condition5 != 0:
#     print(f"{num} is not divisible by 3 and 5")

# Bai 5
# username = "admin"
# password = "12345" 
# print("Welcome to The Ultimate Sercurity System")
# username_input = input("Username: ")
# password_input = input("Password: ")

# if username_input == username and password_input == password:
#     print(f"You are logged in, {username}.")
# else:
#     print("Wrong username or password.")

# Bai 6 
# length_1 = float(input("Input length 1: "))
# length_2 = float(input("Input length 2: "))
# length_3 = float(input("Input length 3: "))

# if length_1 + length_2 > length_3 and length_2 + length_3 > length_1 and length_1 + length_3 > length_2:
#     print("The 3 line segments can form a triangle.")
# else: 
#     print("The 3 line segments cannot form a triangle.")

# Bai 7 
# length_1 = float(input("Input length 1: "))
# length_2 = float(input("Input length 2: "))
# length_3 = float(input("Input length 3: "))
# length1_plus_2 = length_1 + length_2 > length_3
# length2_plus_3 = length_2 + length_3 > length_1
# length1_plus_3 = length_1 + length_3 > length_2

# if length1_plus_2 and length2_plus_3 and length1_plus_3:
#     if length_1**2 == length_2**2 + length_3**2 or length_2**2 == length_1**2 + length_3**2 or length_3**2 == length_1**2 + length_2**2:
#         print("The 3 line segments can form a right triangle.")
#     elif length_1 == length_2 == length_3:
#         print("The 3 line segments can form an eqilateral triangle.")
#         for i in range(3):
#             forward(length_1)
#             left(120)
#         done()    
#     else:
#         print("The 3 line segments can form a triangle.")
# else: 
#     print("The 3 line segments cannot form a triangle.")
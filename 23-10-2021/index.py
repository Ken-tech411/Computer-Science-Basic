import math
# Bai 1
# num1 = int(input("Put a number: "))
# num2 = int(input("Put a number: "))
# num3 = int(input("Put a number: "))

# if (num1 > num2) and (num1 > num3):
#     print(f"The largest number is: {num1}")
# elif (num2 > num1) and (num2 > num3):
#     print(f"The largest number is: {num2}")
# elif (num3 > num1) and (num3 > num2):
#     print(f"The largest number is: {num3}")

# Bai 2

# weight = float(input("Put your weight in kilogram: "))
# height = float(input("Put your height in meter: "))
# bmi = weight / (height ** 2)

# if (bmi < 18.5):
#     print(bmi)
#     print("You are underweight!")
# elif (18.5 <= bmi <= 24.9):
#     print(bmi)
#     print("You are normal!")
# elif (25 <= bmi <= 29.9):
#     print(bmi)
#     print("You are overweight!")
# elif (bmi > 30):
#     print(bmi)
#     print("You are obese!")

# Bai 3

# a = int(input("Put a number: "))
# b = int(input("Put a number: "))
# c = int(input("Put a number: "))

# if a + b > c and b + c > a and a + c > b:
#     print("It can be a triangle!")
# else: 
#     print("It cannot be a triangle!")

# Bai 4
# a = float(input("Input a: "))
# b = float(input("Input b: "))
# c = float(input("Input c: "))

# delta = delta = b**2 - 4 * a * c
# if delta > 0:
#     x1 = (-b + math.sqrt(delta)) / (2 * a)
#     x2 = (-b - math.sqrt(delta)) / (2 * a)
#     print(x1, x2)
# elif a == 0:
#     x1 = (-b) / (2 * a)
#     x2 = x1
#     print(x1, x2)
# else:
#     print("Đổi số đi bạn êy =))))))))")

# Bai 5 
# year = float(input("Put the year: "))
# sodu = [0, 3, 6, 9, 11, 14, 17]
# chia = year % 19

# if year % 4 == 0:
#     print("This is leap year")
# elif (chia in sodu):
#     print("This is leap lunar year")
# else: 
#     print("This is not leap year")

# Bai 6
# practice = float(input("Put your score: "))
# hw_theory = float(input("Put your score: "))
# theory = float(input("Put your score: "))

# total = (0.30 * practice) + (0.30 * hw_theory) + (0.40 * theory)

# if (total >= 5):
#     print("Congrats, you passed")
# else:
#     print("Congrats, you failed. Study again =))))")

# Bai 7 
average = float(input("Input: "))

if average >= 9.0 :
    print("Output: Outstanding")
elif 8.0 <= average <= 8.99 :
    print("Output: Excellent")
elif 7.0 <= average <= 7.99 :
    print("Output: Good")
elif 6.0 <= average <= 6.99 :
    print("Output: Normal")
elif 5.0 <= average <= 5.99 :
    print("Output: Average")
elif 4.0 <= average <= 4.99 :
    print("Output: Poor")
elif average <= 4:
    print("Output: Thằng gà mờ =)))))))")
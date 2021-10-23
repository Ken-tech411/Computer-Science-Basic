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
a = int(input("Put a number: "))
b = int(input("Put a number: "))
c = int(input("Put a number: "))

if a + b > c and b + c > a and a + c > b:
    print("It can be a triangle!")
else: 
    print("It cannot be a triangle!")
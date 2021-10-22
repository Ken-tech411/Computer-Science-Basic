from turtle import *

# bài 1
# from math import floor

# num1 = int((input("Input a number: ")))
# num2 = int((input("Input a number: ")))

# print(f"Cong: {(num1) + (num2)}")
# print(f"Tru: {(num1) - (num2)}")
# print(f"Nhan: {(num1) * (num2)}")

# if num1 == 0 or num2 == 0:
#     print("Cannot divide by zero")
# else:
#     print(f"Chia: {(num1) / (num2)}")

# bài 2
# sec = int(input("Put seconds: "))
# days = sec // int(84600)
# sec = sec % int(84600)

# hours = sec // int(3600)
# sec = sec % int(3600)

# mins = sec // int(60)
# sec = sec % int(60)

# print(f"Conversion: {(days)} day(s) {(hours)} hour(s) {(mins)} minute(s)")

# bài 3
pensize(5)
speed(1)
color("black", "aliceblue")
begin_fill()

for i in range(10):
    left(36)
    forward(100)

end_fill()
done()
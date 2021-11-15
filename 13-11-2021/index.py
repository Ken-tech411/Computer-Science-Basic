# Bai 1
# foods_num = int(input("Nhap so luong mon an: "))
# food_menu = []

# for i in range(foods_num):
#     food_menu.append(input("Food {}: ".format(i+1)))

# for i in food_menu:
#     print(i)

# food_del = input("Do you want to remove any food: ")

# if food_del in food_menu:
#     print(food_del)
#     sure = input("Are you sure you want to remove dat food? Y or N: ")
#     if sure == "Y":
#         food_menu.remove(food_del)
#         print("{} removed".format(food_del))
#     elif sure == "N":
#         print("Canceled")
# elif food_del == "no":
#     for i in food_menu:
#         print(i)
# else:
#     print("{} not found".format(food_del))
# for i in food_menu:
#     print(i)   

# Bai 2
# num = []
# n = int(input("Input number: "))

# for i in range(n):
#     num.append(int(input("Number {}: ".format(i+1))))
# for i in num:
#     print(i, end = ' ')

# s = 0
# for i in num:
#     s += i

# max = num[0]
# for i in num:
#     if i > max:
#         max = i
# print(f"\nSum = {s}\nMax = {max}\nMin = {min(num)}")

# Bai 3
# n = int(input("Input number: "))
# num = []

# for i in range(n):
#     num.append(int(input("Number {}: ".format(i+1))))

# for i in range(len(num)):
#     for j in range(i + 1, len(num)):
#         if num[i] > num[j]:
#             num[i], num[j] = num[j], num[i]
# print(num, end = ' ')
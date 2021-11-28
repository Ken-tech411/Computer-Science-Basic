#Bai 1
# def nam_nhuan(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print("Lear year")
#     else:
#         print("Not leap year")

# def nam_nhuan(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return "Leap year"
#     elif year == 2000 or year == 2400:
#         return "Leap year"
#     else:
#         return "Not lear year"

# year = int(input("Year: "))
# print(nam_nhuan(year))

# Bai 2
# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# def even_odd(num):
#     if num % 2 == 0:
#         print("Even") 
#     else:
#         print("Odd")

# num = int(input("Number: "))
# print(even_odd(num))

# Bai 3
# a = [1, 2, 3, 4, 'a', '5', '7']
# def sum(a):
#     sum = 0
#     for i in range(len(a)):
#         if type(a[i]) == int:
#             sum += a[i]
#         elif a[i].isnumeric():
#             sum += int(a[i])
#     return sum

# print(sum(a))

# Bai 4
word_split = []
def split_word():
    for i in range(len(word)):
        word_split.append(ord(word[i]))
    word_split.sort()
word = input("Input a word: ")
split_word()
for i in word_split:
    print(chr(i), end = " ")
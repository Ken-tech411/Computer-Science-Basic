# Bai 1 
# # Add 2
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(arr)):
#     arr[i] = arr[i] + 2
# print(f"Add 2\t\t: {arr}")

# # Multify 2
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(arr)):
#     arr[i] = arr[i] * 2
# print(f"Multiply bt 2\t: {arr}")

# # Shift 2
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 2
# print(f"Shift 2\t\t: {arr[n:] + arr[:n]}")

# Bai 2
# arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l',
# 'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']

# print(arr[::-1])
# Bai 3
# n = int(input("Input number: "))

# n1, n2 = 0, 1
# count = 0

# if n <= 0:
#     print("Please input a positive integer")
# else:
#     print(f"First {n} Fibonacci number(s):")
#     while count < n:
#         print(n1, end = " ")
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1

# Bai 4
# n = int(input("Number of items: "))
# items = []
# for i in range(n):
#     item = input("Item {}: ".format(i+1))
#     price_item = float(input("Price of items {}: ".format(i + 1)))
#     items.append((item, price_item))

# avg = 0
# for i in range(len(items)):
#     avg += float(items[i][1])
# avg = avg / len(items)
# print(f"\nAverage price: {avg}")

# items_moreavg = []
# for i in range(len(items)):
#     if int(items[i][1]) > avg:
#         items_moreavg.append(items[i])
# print(f"Item(s) above average: {items_moreavg}")

# Bai 5
# sentence = input("Write a sentence: ")
# word_list = sentence.split(' ')
# number_of_words = len(word_list)
# print(f"Number of unique words: {number_of_words}")
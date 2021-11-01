# for i in range(11):
#     print(i, end=" ")

# print("\n")
# for i in range(100, 107):
#     print(i, end=" ")

# print("\n")
# x = 10
# for i in range(8):
#     x -= 1
#     print(x, end=" ")

# for i in range(21):
#     if i % 3 == 0:
#         print(i)

n = int(input("Put a number: "))
count = 0

# for i in range(n + 1):
#     print(i)

while n != 0:
    count += 1 
    n = n // 10
print(count)

# for i in range(1, n + 1):
#     count += i/(i+1)

# print(round(count, 4))

# if num <= 0:
#     print(False)
# total = 0
# for i in range(1, num):
#     if num % i == 0:
#         total += i
# if total == num:
#     print(True)
# else:
#     print(False)


# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("#", end=" ")
#     print("\n")

# x = int(input("Input: "))
# n = int(input("Input: "))

# for i in range(len(x)):
#     print(x[len(x) - i - 1], end="")

# for num in range(x, n + 1):  
#    if num > 1:  
#        for i in range(2,n):  
#            if (n % i) == 0:  
#                break  
#        else:  
#            print(n)  

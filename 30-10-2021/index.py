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
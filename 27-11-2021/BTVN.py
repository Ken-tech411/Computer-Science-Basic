from datetime import datetime
# Bai 1 
# def is_int(num):
#     try:
#         val = int(num)
#         print(f"{num} is an interger")
#     except ValueError:
#         try:
#             val = float(num)
#             print(f"{num} is not an interger")
#         except ValueError:
#             print(f"{num} is not a number")

# num = input("Input number: ")
# is_int(num)

# Bai 2
# def is_prime(num):
#     for i in range(2, int(num / 2) + 1):
#         if (num % i) == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# num = int(input("Input character: "))

# if num > 1:
#     is_prime(num)
# else:
#     print(f"{num} is not a prime number")

# Bai 3
# def prime(num):  
#     for i in range(2, num // 2 + 1):  
#         if(num % i == 0):  
#             return False
#     return True
  
# num = int(input("Enter character: "))  
# i = 2  
# prime_num = [] 
# while True:  
#     if(prime(i)):  
#         prime_num.append(i) 
#         if(len(prime_num) == num): 
#             break 
#     i += 1 
# print(f"First {num} prime numbers:", end=" ") 
# print(*prime_num)

# Bai 4
def special_expresso(num):
    count = 1
    if (num == 1 or num == 0):
        return count
    else:
        for i in range(2, num + 1):
            count *= i
        return count

num = int(input("Input number: "))

sum = 0
for i in range(1, num + 1):
    sum += special_expresso(i) / i
print(f"Result: {int(sum)}")

# Bai 5
# now = datetime.now()
# print(f"Today is {now.strftime('%Y/%m/%d')}\nTime right now: {now.strftime('%H:%M:%S')}")

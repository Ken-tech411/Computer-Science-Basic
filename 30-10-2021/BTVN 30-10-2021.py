from turtle import *
# Bai 1
n = int(input("Input number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("#", end=" ")
    print("\n")

# Bai 2  
n = float(input("Input number: "))

while n <= 0:
    n = float(input("Input number: "))
print("Thank you")

# Bai 3  
n = int(input("Input number: "))
count = 1

if n == 0:
    print("0! = 1")
elif n >= 1:
    for i in range(1, n + 1):
        count *= i
    print(f"{n}! = {count}")
elif n < 0:
    print("Invalid")

# Bai 4
n = int(input("Input number: "))
num = n
count = 0

while n > 0:
    digit = n % 10
    count += digit
    n = n // 10
print(f"Sum of digits of {num} is {count}")

# Bai 5
list = []
for num in range(1000, 1110): 
    sn = str(num) 
    listsn = [] 
    for i in range(4): 
        listsn += [int(sn[i])] 
    if sum(listsn) == 9: 
        list += [num]
print(f"Numbers with sum of digits = 9:\n{list}")

# Bai 6
edges = int(input("Input number of edges: "))

for i in range(edges):
    forward(100)
    left(int(360) / edges)
done()

# Bai 7
for i in range(10, 1000, 10):
    circle(- i, -180)
done()
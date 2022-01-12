# Bai 1
# with open("./names.txt", "r") as file:
#     print(f"List of names:")
#     for i in file.readlines():
#         print(f"- {i.strip()}")

# Bai 2
# input = input("Input file name: ")

# try:
#     with open(input, "r") as file:
#         print(f"File content:")
#         for i in file.readlines():
#             print(f"{i.strip()}")
# except FileNotFoundError:
#     print(f"File not found.")

# Bai 3 
import datetime
date = datetime.datetime.now()

# print("== Input file content below ==")
# while True:
#     line = input("")
#     if line == "":
#         break
#     with open("./user-inputs.txt", "a") as file:
#         file.write(f"{line}\n")
# print("== Input recorded in user-inputs.txt ==")

# Bai 4
# print("== Input file content below ==")
# with open("./input-logs.txt", "a") as file:
#     file.write(f"\nInputs at {date}\n")
# while True:
#     line = input("")
#     if line == "":
#         break
#     with open("./input-logs.txt", "a") as file:
#         file.write(f"{line}\n")
# print("== Input recorded in input-logs.txt ==")

# Bai 5
print("Give the correct answers to get points.")
with open("./question-bank.txt", "r") as file:
    points = 0
    for i in file.readlines():
        s = i.split(",")
        print(f"{s[0]}", end="")
        answer = s[1].strip()
        if input() == answer:
            points += 1
    with open("question-bank.txt", 'r') as file:
        for count, line in enumerate(file):
            pass
    print(f"== You got {points}/{count + 1} points ==")
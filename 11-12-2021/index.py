# Bai 1
com_quantity = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30,
}

# x = input("Enter the name of the computer: ").upper()

# try:
#     print(com_quantity[x])
# except KeyError:
#     print("We don't have this brand of computer")

# Bai 2
# user = {
#     "name": "Light",
#     "age": 17,
#     "strength": "8",
#     "defense": "10",
#     "hp": 100,
#     "backpack": ["Shield", "Bread Loaf"],
#     "gold": 100,
#     "level": 2
# }

# user.update({"gold": user["gold"] + 50})
# user["backpack"].append("FlintStone")
# user.update({"pocket": ["Monsterdilla", "Flashlight"]})
# print(user)

# Bai 3
for i in range(3):
    com_brand = input("Input a computer brand: ").upper()
    com_quantities = int(input("Input the quantity of that brand: "))
    com_quantity.update({com_brand: com_quantities})

sort_orders = sorted(com_quantity.items(), key = lambda x : x[-1], reverse = True)

for i in sort_orders:
    print(i[0], ":", i[1])

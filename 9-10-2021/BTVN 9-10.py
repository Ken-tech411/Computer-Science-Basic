import turtle
# Bai 1
name = input("Input your name: ")
print(f"Welcome, {name}") 

# # Bai 2
first_name = input("First name: ")
last_name = input("Last name: ")
phone_number = input("Phone number: ")

print(f"Your registered name is {first_name} {last_name} \nYour phone number is {phone_number}")

# Bai 3
name_input = input("Name: ")
birthdate = input("Birthdate: ")
print(f"Name\t\t: \t{name_input} \nBirthdate\t: \t{birthdate}")

#Bai 4
year = input("What year is it? \n")
print(f"""
                            . : .
                          '.  :   .'
     HAPPY NEW YEAR    .    '.:.'    .  
     !!! {year} !!!      .    .':'.    .
                          .'  :    '. 
                          '   :   '   
""")

# Bai 5
wn = turtle.Screen()

pen = turtle.Turtle()

pen.speed(1)
pen.pendown()

pen.forward(100)
pen.left(120)
pen.forward(100)

pen.forward(100)
pen.left(120)
pen.forward(100)

pen.forward(100)
pen.left(120)
pen.forward(100)

pen.penup()
turtle.done()

# Bai 6
turtle.Screen()

pen = turtle.Turtle()

pen.speed(2)
pen.pendown()

for i in range(0, 4):
    pen.forward(100)
    pen.left(90)
    pen.forward(100)

pen.penup()
pen.goto(0, -20)
pen.pendown()
pen.pensize(5)

for i in range(0, 4):
    pen.forward(120)
    pen.left(90)
    pen.forward(120)

pen.penup()
turtle.done()

# Bai 7
turtle.Screen()

pen = turtle.Turtle()

pen.speed(3)
pen.pendown()

for i in range(0, 4):
    pen.forward(100)
    pen.left(90)
    pen.forward(100)

pen.penup()
pen.goto(0,-45)
pen.pendown()
pen.left(45)
for i in range(0, 4):
    pen.forward(200)
    pen.left(90)

pen.penup()
turtle.done()
#Bai 1, 2, 3
numbers_1 = {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
    'VI': 6,
    'VII': 7,
    'VIII': 8,
    'IX': 9,
    'X': 10,
}

numbers_2 = {
    'XI': 11,
    'XII': 12, 
    'XIII': 13,
    'XIV': 14, 
    'XV': 15,
    'XVI': 16, 
    'XVII': 17, 
    'XVIII': 18, 
    'XIX': 19, 
    'XX': 20}

numbers = {**numbers_1, **numbers_2}
input_number = input('Input a Roman number: ').upper()

try:
    print(f"Arabic number: {numbers[input_number]}")
except KeyError:
    print('Not found.')

# number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
# 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

# number = {
    
# }
# for i in range(number_list.__len__()):
#     number.update({number_list[i]: numbers[number_list[i]]})

# try:
#     input_number = input('Input a Roman number: ').upper()
#     print(f"Arabic number: {number[input_number]}")
# except KeyError:
#     print('Not found.')

# Bai 4
# students = [{'firstName': 'Nikki', 'lastName': 'Roysden'},
#             {'firstName': 'Mervin', 'lastName': 'Friedland'},
#             {'firstName': 'Aron', 'lastName': 'Wilkins'}]
# print("List of students:")
# for i in range(students.__len__()):
#     print(f"- {students[i]['firstName']} {students[i]['lastName']}")

# Bai 5
# names = {
#     'students': [
#         {'firstName': 'Nikki', 'lastName': 'Roysden'},
#         {'firstName': 'Mervin', 'lastName': 'Friedland'},
#         {'firstName': 'Aron', 'lastName': 'Wilkins'}
#     ],

#     'teachers': [
#         {'firstName': 'Amberly', 'lastName': 'Calico'},
#         {'firstName': 'Regine', 'lastName': 'Agtarap'}
# ]
# }

# print("List of students:")
# for i in range(len(names['students'])):
#     print(f"- {names['students'][i]['firstName']} {names['students'][i]['lastName']}")

# print("List of teachers:")
# for i in range(len(names['teachers'])):
#     print(f"- {names['teachers'][i]['firstName']} {names['teachers'][i]['lastName']}")

# Bai 6
# all_char = {}
# input = input("Input sequence: ")

# for i in input:
#     if i in all_char:
#         all_char[i] += 1
#     else:
#         all_char.update({i:1})
# print(f"Frequency of characters: \n{all_char}")
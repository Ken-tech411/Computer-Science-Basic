# text = "Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data.It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so.Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, and computer vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks."

# file = open("./text.txt", "a")

# with open("text.txt", "a") as file:
#     new_file = text.replace(",", "")
#     new_file = text.split(".")
#     new_file = "\n".join(new_file)

#     s = new_file.split()
#     all_char = {}
#     for i in s:
#         if i in all_char:
#             all_char[i] += 1
#         else:
#             all_char.update({i:1})
#     file.write(new_file)
#     for i in all_char:
#         file.write(f"{i}: {str(all_char[i])}\n")
# file.close()

file = open("./in.pnm", "r")

s = file.read().replace("\n", " ").split(" ")

# all_char = {}
# for i in s:
#     if i in all_char:
#         all_char[i] += 1
#     else:
#         all_char.update({i:1})
# file.close()

# with open("./bruh.txt", "w") as file:
#     sort_orders = sorted(all_char.items(), key = lambda x : x[-1], reverse = True)
#     for i in sort_orders:
#         file.write(f"{i[0]}: {str(i[1])}\n")

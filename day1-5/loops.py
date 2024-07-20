# #
# # #list with loops
# # fruits = ["apple","banana","orange"]
# #
# # for fruit in fruits:
# #     print(fruit)
# #     print(fruit + " pie")
# #
#
# #input
#
# student_scores = input("enter the scores: \n").split()
#
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#
# high_score = 0
#
# for score in student_scores:
#     if score > high_score:
#         high_score = score
#
# print(f"the highest score in the class is {high_score}")

# sum_total = range(1,101)
#
# total = 0
#
# for total1 in sum_total:
#     total += total1
# print(f"the total is {total}")


sum_total = int(input("enter number between 1 and 100\n"))
sum = 0
for number in range(2,sum_total+1,2):
    sum += number
print(f"the total is {sum}")

















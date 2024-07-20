import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

ascii = [rock,paper,scissors]

user_choice = int(input("Enter a number between 0 and 2: \n"))
computer_choice = random.randint(0,2)

print(f"computer choose {computer_choice} \n {ascii[computer_choice]}")


if user_choice >=3 or user_choice < 0:
    print("you entered invalid number! oops")
elif user_choice == 0 and computer_choice ==2:
    print("you win!")










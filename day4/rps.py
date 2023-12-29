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
         _______)
         ________)
        ________)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
         _______)
         ________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print ("You typed an invalid number, you lose!")
    

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)


if user_choice >= 3 or user_choice < 0:
    print ("You typed an invalid number, you lose!")
elif user_choice ==2 and computer_choice==0 :
    print("You loose!")
elif user_choice ==0 and computer_choice==2 :
    print("You win!")
elif user_choice>computer_choice:
    print("You win!")
elif user_choice<computer_choice:
    print("You loose!")
else:
    print("draw")




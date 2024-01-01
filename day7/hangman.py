stages =['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
  ''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
  ''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
  ''', '''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========
  ''', '''
  +---+
  |   |
  0   |
  |   |
      |
      |
=========
  ''', '''
  +---+
  |   |
  0   |
      |
      |
      |
=========
  ''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
  '''] 

lives = 6


import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"P.s.: the word is:{chosen_word}")
hint = []
for _ in range(0, len(chosen_word)):
        hint+= "_"  
print(hint)
test=True
while test== True:
    guess = input("Guess a letter(lowercase): ")
    order = 0
    for i in chosen_word:
        order +=1
        if guess == i:

            hint[order-1] = i
    if guess not in chosen_word:
        lives-=1
    print(stages[lives])
    print(hint)

    if "_" not in hint:
        test= False
        print(f"You win!{ "".join(hint)} ")
    elif lives<=0:
         test= False
         print(f"You loose!{ "".join(hint)} ")


         
        



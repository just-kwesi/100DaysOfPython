import random;
from hangman_words import word_list;
from art import stages,logo;

#An array of words for the game
# words = ["baboon","horse","proud"];

chosenWord = random.choice(word_list);
print(logo)

word = list("_" * len(chosenWord));

lives = 6;
win = False;

while (lives>=0) and win ==False :
  
  chck = False;
  guess = input("Guess a letter: ").lower();

  for index in range(len(chosenWord)):
    if(guess == chosenWord[index]):
      word[index] = guess;
      chck = True;

  if(chosenWord == "".join(word)) :
    win = True
  
  print(word);
  if(chck == False):
    print(f"You guessed the letter {guess}, that's not in the word. You lose a life.")
    lives-=1;
    print(stages[lives])




if (win):
  print('Congrats you won the game!!') 
else:
 print("Game over, you lost");



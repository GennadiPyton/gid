import random

guesses = 0    #Number of tries to guess.
print ("Welcome to Guess Me!")
print ("\nYou have five guesses, choose letter and guess a word.")
print("\nAll of luck!")

def rand_word():
       f = open('vop.txt', 'r').readlines()  #Sowpods is library with some random words 
       return random.choice(f).strip()                                    

word = rand_word()
print(word)                 #I printed a word just so i can test if is working.

correct = word
lenght = len(word)       #I want to tell them how many letters a word contain
new_length = str(lenght) 

Guess = input("The word is " + new_length + " letters long. Guess a letter: ")

while guesses < 5:
       guesses += 1
       guess = input("The word is " + new_length + " letters long. Guess a letter: ")
       if guess not in word:
           print("Sorry, this letter is not in word.")
       else:
           print("Correct, word contain this letter!")
       if guesses == 5:
           final_answer = input("You ran out of guesses, what is your answer?")
           if final_answer == correct:
               print("That's correct, congratulations you won!")
           else:
               print("Sorry, correct word is" + " " + word + " ,you can try again!")
               

import random

guesses = 0    #Number of tries to guess.
print ("Welcome to Guess Me!")
print ("\nYou have five guesses, choose letter and guess a word.")
print("\nAll of luck!")
 
def get_guestion():
       f = open('vop.txt', 'r').readlines()  #Sowpods is library with some random words 
       return random.choice(f).strip()                                    

guestion = get_guestion()
print(guestion)                 #I printed a word just so i can test if is working.

correct =guestion 
lenght = len(guestion)       #I want to tell them how many letters a word contain
new_length = str(lenght) 

Guess = input("The word is " + new_length + " letters long. Guess a letter: ")                

while guesses < 5:
       guesses += 1
       guesses = input("The word is " + new_length + " letters long. Guess a letter: ")
       if guesses not in new_length:
           print("Sorry, this letter is not in word.")
       else:
           print("Correct, word contain this letter!")
       if guesses == 5:
           final_answer = input("You ran out of guesses, what is your answer?")
           if final_answer == new_length:
               print("That's correct, congratulations you won!")
           else:
               print("Sorry, correct word is" + " " + new_length + " ,you can try again!")













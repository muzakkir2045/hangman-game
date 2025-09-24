
""" Hangman Game """

import random
from collections import Counter

someWords = '''apple banana mango strawberry orange grape 
pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
word = random.choice(list(map(lambda n: n.strip('\n'), someWords.split(' '))))

if __name__ == '__main__':
    print("Guess the word! Hint: word is a name of a fruit")
    for i in word:
        print("_", end = ' ')  # Printing empty spaces
    print()
    playing = True
    letterGuessed = ''     # -> list for storing the guessed letters
    chances = len(word) + 2
    correct,flag = 0 ,0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1
            try:
                guess = str(input("Enter a letter to guess: "))
            except:
                print("Enter only a letter!")
                continue
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guesses that letter')
                continue
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end= ' ')
                    correct += 1
                elif (Counter(letterGuessed)) == Counter(word):
                    print(f"The word is : {word}")
                    flag = 1
                    print('Congratulations, You won!')
                    break    # To break out of the for loop
                else:
                    print('_', end = ' ')        
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print("You lost! Try again..")
            print(f"The word was {word}")
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()

            
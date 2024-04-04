import random
def hangman():
    word_list = ['inova','jaguar','audi','mercedes','creta','defender']
    random_word = random.choice(word_list)
    guessed_word = ''
    chance = 5
    while True:
        output = ''
        for i in random_word:
            if i in guessed_word:
                output = output + i
            else:
                output = output + '_'
        if random_word == output:
            print('You won !!')
            break

        print(output)
        guess = input('Enter the letter:')[0]
        guessed_word = guessed_word + guess
        
        if guess not in random_word:
            chance -= 1
            if chance != 0:
              print('You guessed wrong !!')
            else:
                print('You Lost !!')
        else:
            print('You guessed right !!')
        print(f"Chance left:{chance}")

        if chance == 5:
            print('''
                   --------
                  ''')

        elif chance == 4:
            print('''
                       O
                  ''')
            
        elif chance == 3:
             print('''
                       O
                       |
                  ''')
             
        elif chance == 2:
             print('''
                       O
                       |
                      / \\
                  ''')
             
        elif chance == 1:
             print('''
                     \_O
                       |
                      / \\
                  ''')
             
        elif chance == 0:

            print('''
                     \_O_/
                       |
                      / \\
                  ''')
            break
print('''
-> press 1 to PLAY:-
-> press 2 to EXIT:-
''')
ch = int(input('Enter your choice:'))
if ch==1:
    print('You have 5 chance to guess the word !!')
    hangman()
else:
    pass
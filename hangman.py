def welcome():
    player_name = input('Hi! What is your name? ')
    need_explanation = input('Welcome {}! Do you know how to play hangman? Y/N '.format(player_name))
    print('------------------')
    while ['Y','N'].count(need_explanation.upper()) == 0:
        need_explanation = input('Please choose Y or N ')
    if need_explanation.upper() == 'N':
        print('Computer will generate a hidden word, you have to guess what the word is letter by letter.')
        print('You may get some letters wrong, but if it is more than 5 times, it is game over.')
        print('Good luck!')
    else: print("Let's start!")

welcome()

word_list = ['word', 'useless', 'appliance', 'trot', 'stain', 'blushing', 'immense', 'lip', 'file', 'festive', 'attractive', 'sign']
for word in word_list:
    i = word_list.index(word)
    word_list[i] = word.upper()

from random import randint

play_word = []
full_word = ''
shown = []
score = 0

def generate_word():
    global play_word
    global full_word
    global shown
    play_word.clear()
    word_index = randint(0,len(word_list)-1)
    generated_word = word_list[word_index].upper()
    list_of_characters = list(generated_word)
    play_word = list_of_characters
    full_word = ''.join(play_word)
    for letter in play_word:
        shown.append('_')
    print('Your word is {}'.format(shown))

def make_guess():
    generate_word()
    global score
    global word_list
    global play_word
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVW'
    tries = 5
    while '_' in shown:
        guess = input('Make your guess (1 letter only) ')
        print('---------RESULT---------')
        guess_cap = guess.upper()
        if guess_cap in alphabet and len(guess) == 1:
            if guess_cap in play_word:
                for i in range(0,len(play_word)):
                    if play_word[i] == guess_cap:
                        shown[i] = guess_cap
                        score += 1
                if '_' not in shown:
                    print('You win!')
                    word_list.remove(full_word)                        
            else:
                print('The letter {} is not in the word'.format(guess_cap))
                tries -= 1
                score -= 1
                if tries == 0:
                    print('You lose. The word is ' + full_word)
                    print('Your final score ' , score)
                    break
            alphabet = alphabet.replace(guess_cap,'')
            print('Available characters ' + alphabet)
            score = len(full_word) - shown.count('_')
            print('Score: ' , score, '    Remaining tries: ', tries)
            print(shown)
        else: print('Input invalid, please try again!')
        print('------------------')

def ccontinue():
    global play_word
    make_guess()
    play_again = input('Do you want to play again? Y/N')
    while play_again.upper() not in ['Y', 'N']:
        play_again = input('Invalid input, please try again. Y/N')
    if play_again.upper() == 'Y':
        make_guess()
    elif play_again.upper() == 'N':
        print('Your total score is ' , score)

ccontinue()
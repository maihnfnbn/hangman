def welcome():
    player_name = input('Hi! What is your name? ')
    need_explanation = input('Welcome {}! Do you know how to play hangman? Y/N '.format(player_name))
    while ['Y','N'].count(need_explanation.upper()) == 0:
        need_explanation = input('Please choose Y or N ')
    if need_explanation.upper() == 'N':
        print('Computer will generate a hidden word, you have to guess what the word is letter by letter.')
        print('You may get some letters wrong, but if it is more than 5 times, it is game over.')
        print('Good luck!')
    else: print("Let's start!")
welcome()

word_list = ['word', 'useless', 'appliance', 'trot', 'stain', 'blushing', 'immense', 'lip', 'file', 'festive', 'attractive', 'sign']

from random import randint
def generate_word():
    word_index = randint(0, len(word_list))
    generated_word = word_list[word_index]
    list_of_characters = list(generated_word)
    shown = []
    for letter in list_of_characters:
        shown.append('_')
    return shown

print('Your first word is {}'.format(generate_word()))


def guess(letter):
    pass

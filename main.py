import random

def get_random_word(min_length, max_length):
    file_path = r'E:\projects\hangman-python\words.txt'
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if min_length <= len(line.strip()) <= max_length]
        
        if not words:
            print(f"No words found in the specified size range.")
            return None

        random_word = random.choice(words)
        print(random_word)
        return random_word
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def game(word):
    word_length = len(word)
    dash = ['_'] * word_length
    timer = 6

    while True:
        print('__________________________')
        print(" ".join(dash))
        print('__________________________')
        
        guess = input('Guess: ')
        if guess in word:
            for i in range(word_length):
                if guess == word[i]:
                    dash[i] = guess
        else:
            timer -= 1
            print(f'Incorrect chances remaining: {timer}')
        
        if timer == 0 or '_' not in dash:
            return timer

def choose_level():
    while True:
        level = input('Choose level: 1 - Easy, 2 - Medium: ')
        if level == '1':
            return get_random_word(4, 4), level
        elif level == '2':
            return get_random_word(5, 8), level
        else:
            print('Choose a correct option.')

if __name__ == "__main__":
    print('---------------------------------')
    print('#### Welcome To Hangman Game ####')
    print('---------------------------------')

    selected_word, selected_level = choose_level()
    result = game(selected_word)

    if result == 0:
        print(f"Sorry, you lost. The word was: {selected_word}")
    else:
        print(f"Congratulations! You guessed the word: {selected_word}")

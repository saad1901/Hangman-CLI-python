import random

def get_random_word(file_path, min_length, max_length):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if min_length <= len(line.strip()) <= max_length]
        
        if not words:
            print(f"No words found in the specified size range.")
            return None

        random_word = random.choice(words)
        return random_word
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

file_path = r'hangman-python\words.txt'
min_length = 5
max_length = 8
word = get_random_word(file_path, min_length, max_length)

# print(word)
print('\n')
print('#### Welcome To Hangman Game ####')
print('\n')
level = input('choose level 1:Easy 2:Medium')


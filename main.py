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
        return random_word
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# # min_length = 5
# # max_length = 8
# word = get_random_word(min_length, max_length)
word = ''
null = ''
# print(word)
print('---------------------------------')
print('#### Welcome To Hangman Game ####')
print('---------------------------------')

def choose_level():
    global word
    level = input('choose level 1:Easy 2:Medium : ' )
    if level == "1":
        word = get_random_word(4,4)
        # print('word is ',word)
    elif level == '2':
        word = get_random_word(5,8)
        # print(word)
    else:
        print('!choose correct option')
        choose_level()

choose_level()
# print(word)

def game(words):
    for i in words:
        null.append('_')
    print(null)

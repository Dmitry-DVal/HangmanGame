import random
from draw_hangman import draw_hangman

GREETING = "Добро пожаловать в игру 'Виселица'!\nУ Вас есть 6 попыток, чтобы отгадать слово"
SaveAttempts = "Ваша попытка не сгорает"
CONGRATULATIONS = "Поздравляю, Вы победили!!!"
CONDOLENCE = "Выши попытки закончились, вы проиграли("
ALPHABIT = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
WrongSymbol = "Вы ввели не подходящий символ"
EnterLetter = "Введите букву русского алфавита:\n"
UsedLetter = "Вы уже использовали букву"
LastMessage = "Загаданное слово было:"
NoLetter = "- этой буквы нет в загаданном слове"
YesLetter = "- эта буква есть в загаданном слове"
LenWord = "букв - длина загаданного слова"
ShowingUsedLetters = "Использованные буквы:"
ShowingAttempts = "Осталось попыток:"
WillingnessPlay = "Вы хотите сыграть еще раз?\nД - Да\nН - Нет"


def choice_random_word():
    with open('word_list.txt', encoding='utf-8') as file:
        random_word = list(random.choice([word.strip("',") for word in file.read().upper().split()]))
    return random_word


def check_input_letter(letter):
    if letter not in ALPHABIT or len(letter) > 1:
        print(WrongSymbol)
        print(SaveAttempts)
        return True
    else:
        return False


def check_used_letters(letter, used_letters):
    if letter in used_letters:
        print(UsedLetter, letter)
        print(SaveAttempts)
        return True
    else:
        return False


def check_letter_in_random_word(letter, random_word, attempts, guessed_letters, used_letters):
    if letter not in random_word:
        attempts -= 1
        print(letter, NoLetter)
        print(draw_hangman(attempts))
        print(SaveAttempts, attempts)
        print(*guessed_letters)
    else:
        for i in range(random_word.count(letter)):
            ind = random_word.index(letter)
            random_word[ind] = '*'
            guessed_letters[ind] = letter
        print(letter, YesLetter)
        print(draw_hangman(attempts))
        print(*guessed_letters)
    used_letters.add(letter)
    print(ShowingUsedLetters, *used_letters)
    return attempts


def check_end_of_game(cancelled_letters, my_flag, attempts):
    if cancelled_letters == my_flag:
        print(CONGRATULATIONS)
        return True
    elif attempts == 0:
        print(CONDOLENCE)
        print(LastMessage, "".join(my_flag))
        return True
    else:
        return False


# Приветствие
def print_start_massege(random_word, attempts, guessed_letters):
    print(GREETING)
    print(draw_hangman(attempts))
    print(*guessed_letters)
    print(len(random_word), LenWord)


def get_initial_data():
    random_word = choice_random_word()  # Выбор рандомного слова
    my_flag = random_word.copy()  # Копия рандомного слова
    attempts = 6  # Количество попыток
    guessed_letters = list("_" * len(random_word))  # Список отгаданных букв
    used_letters = set()  # Множество использованных букв
    return random_word, my_flag, attempts, guessed_letters, used_letters


def gameplay():
    random_word, my_flag, attempts, guessed_letters, used_letters = get_initial_data()

    print_start_massege(random_word, attempts, guessed_letters)  # Приветствие

    while attempts > 0:
        letter = input(EnterLetter).upper()
        if check_input_letter(letter):
            continue
        elif check_used_letters(letter, used_letters):
            continue
        attempts = check_letter_in_random_word(letter, random_word, attempts, guessed_letters, used_letters)
        if check_end_of_game(guessed_letters, my_flag, attempts):
            break
        else:
            continue


def check_play_again():
    print(WillingnessPlay)
    answer = input().upper()
    return answer == 'Д'


gameplay()

while check_play_again():
    gameplay()

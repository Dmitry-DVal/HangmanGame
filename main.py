import random
from draw_hangman import draw_hangman


def choice_random_word():
    with open('word_list.txt', encoding='utf-8') as file:
        random_word = list(random.choice([word.strip("',") for word in file.read().upper().split()]))
    return random_word


def check_input_letter(letter):
    if letter not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' or len(letter) > 1:
        print(f'Вы ввели не подходящий символ')
        print(f'Ваша попытка не сгорает')
        return True
    else:
        return False


def check_used_letters(letter, used_letters):
    if letter in used_letters:
        print(f'Вы уже использовали букву {letter}')
        print(f'Выша попытка не сгорает')
        return True
    else:
        return False


def check_letter_in_random_word(letter, random_word, attempts, cancelled_letters, used_letters):
    if letter not in random_word:
        attempts -= 1
        print(f"Буквы '{letter}' нет в загаданном слове")
        print(draw_hangman(attempts))
        print(f'Осталось попыток: {attempts}')
        print(*cancelled_letters)
        used_letters.append(letter)
    else:
        used_letters.append(letter)
        for i in range(random_word.count(letter)):
            ind = random_word.index(letter)
            random_word[ind] = '*'
            cancelled_letters[ind] = letter
        print(f"Буква '{letter}', есть в слове")
        print(draw_hangman(attempts))
        print(*cancelled_letters)
    print(f"Использованные буквы: {used_letters}")
    return attempts


# Приветствие
def print_start_massege(random_word, attempts, cancelled_letters):
    print("Добро пожаловать в игру 'Виселица'!")
    print(draw_hangman(attempts))
    print(*cancelled_letters)
    print(f"Загаданное слово состоит из {len(random_word)} букв")
    print(f"У Вас есть 6 попыток")


def gameplay():
    random_word = choice_random_word()  # Выбор рандомного слова из словаря word_list
    my_flag = random_word.copy()  # Копия рандомного слова
    attempts = 6  # Количество попыток
    cancelled_letters = list("_" * len(random_word))  # Список отгаданных букв
    used_letters = []  # Список использованных букв

    print_start_massege(random_word, attempts, cancelled_letters)  # Приветствие

    while attempts > 0:
        letter = input("Введите букву русского алфавита:\n").upper()

        if check_input_letter(letter):
            continue
        elif check_used_letters(letter, used_letters):
            continue
        attempts = check_letter_in_random_word(letter, random_word, attempts, cancelled_letters, used_letters)
        if cancelled_letters == my_flag:
            print(f"Поздравляю, Вы победили!!!")
            break
        elif attempts == 0:
            print(f"Выши попытки закончились, вы проиграли(")
            print(f'Загаданное слово было: {my_flag}')
            break


def check_play_again():
    print(f'Вы хотите сыграть еще раз?\nД - Да\nН - Нет')
    answer = input().upper()
    return answer == 'Д'


gameplay()

while check_play_again():
    gameplay()

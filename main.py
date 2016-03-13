# -*- coding: utf-8 -*-

import random

# Constants
ADJECTIVES = 'adjectives'
ADVERBS = 'adverbs'
VERBS = 'verbs'
NOUNS = 'nouns'

AFFIRMATIVE = 'affirmative'
INTERROGATIVE = 'interrogative'
NEGATIVE = 'negative'
CONDITIONAL = 'conditional'
MOTIVE = 'motive'

ADJECTIVES_DICT = 'data/' + ADJECTIVES + '.txt'
ADVERBS_DICT = 'data/' + ADVERBS + '.txt'
VERBS_DICT = 'data/' + VERBS + '.txt'
NOUNS_DICT = 'data/' + NOUNS + '.txt'


def generate_structure():
    """
    Генерация структуры предложений.
    :return: dict
    """
    return {
        AFFIRMATIVE: [ADJECTIVES, NOUNS, VERBS, ADVERBS, ADJECTIVES, NOUNS, '.'],
        INTERROGATIVE: [VERBS, ADJECTIVES, NOUNS, ADVERBS, ADJECTIVES, NOUNS, '?'],
        NEGATIVE: [ADJECTIVES, NOUNS, VERBS, ADVERBS, ADJECTIVES, NOUNS, 'nicht', '.'],
        CONDITIONAL: [ADJECTIVES, '.'],
        MOTIVE: [ADJECTIVES, '!']
    }


def load_data(filename):
    """
    Чтение словаря из файла
    :param filename: имя файла
    :return:
    """
    with open(filename, 'r') as file:
        data = file.read()
    data = data.split()
    return data


def get_dictionary():
    """
    Генерация словаря
    :return:
    """
    return {
        ADJECTIVES: load_data(ADJECTIVES_DICT),
        ADVERBS: load_data(ADVERBS_DICT),
        VERBS: load_data(VERBS_DICT),
        NOUNS: load_data(NOUNS_DICT)
    }


def get_random_word(dictionary):
    """
    Получить случайное слово из словаря
    :param dictionary: словарь
    :return: слово
    """
    return random.choice(dictionary)


def generate_sentence(dictionary, structure):
    """
    Генератор предложений
    :param dictionary: словарь
    :param structure: структура предложения
    :return: предложение
    """
    result = ''
    for count, item in enumerate(structure, start=1):
        if item in dictionary:
            result += get_random_word(dictionary[item])
        elif item == structure[-1]:
            result += item
        else:
            result += item
        if count < len(structure) - 1:
            result += ' '
    return result.capitalize()


def main():
    # Генерация словаря
    dictionary = get_dictionary()

    # Генерация структуры текста
    structures = list(generate_structure().values())
    structures = random.sample(structures, len(structures))

    # Генерация текста
    text = []
    for sentence in structures:
        text.append(generate_sentence(dictionary, sentence))

    # Вывод текста
    print(' '.join(text))


if __name__ == '__main__':
    main()


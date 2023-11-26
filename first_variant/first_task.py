class Scrabble:

    def __init__(self):
        self.__letters_dict = {
            'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
            'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
            'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
            'Й': 4, 'Ы': 3,
            'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
            'Ш': 8, 'Э': 8, 'Ю': 8,
            'Ф': 10, 'Щ': 10, 'Ъ': 10
        }

    def get_result(self):
        word = input('Enter ur word: ').upper()
        letters = []
        for item in word:
            letters.append(item)

        count_score = 0

        for letter in letters:
            for key, value in self.__letters_dict.items():
                if letter == key:
                    count_score += value

        print(f'Result: {count_score}')

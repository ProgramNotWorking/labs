class Correction:

    @staticmethod
    def get_result():
        original_string = input('Enter something: ')
        result_string = ''
        for letter in range(0, len(original_string)):
            first = original_string[letter - 2]
            second = original_string[letter - 1]

            if letter == 0:
                result_string += original_string[0].upper()
            elif letter == 1 or letter == 2:
                result_string += original_string[letter]
            elif first == '?' or first == '!' or first == '.' and second == ' ':
                result_string += original_string[letter].upper()
            elif second == ' ' and original_string[letter] == 'i':
                result_string += original_string[letter].upper()
            else:
                result_string += original_string[letter]

        print(result_string)

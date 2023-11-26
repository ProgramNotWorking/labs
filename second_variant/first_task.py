class Email:

    def __init__(self):
        self.__emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
                  'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
                  'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
                  'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
                  'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
                  'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

        self.__students_list = self.__get_students_list()

    def __get_students_list(self) -> list:
        result_list = []

        for key in self.__emails:
            for value in self.__emails.get(key):
                result_list.append(value)

        result_list.sort()

        return result_list

    def get_result(self):
        result_list = []

        for student in self.__students_list:
            for key in self.__emails:
                for value in self.__emails.get(key):
                    if value == student:
                        result_list.append(f'{value}@{key}')

        print('\n')
        for item in result_list:
            print(item)

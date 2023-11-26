class Song:

    def __init__(self):
        self.__second_const_string = 'my true love sent to me:'
        self.__last_const_string = 'And a partridge in a pear tree.'
        self.__days_dict = {
            1: 'first',
            2: 'second',
            3: 'third',
            4: 'fourth',
            5: 'fifth',
            6: 'sixth',
            7: 'seventh',
            8: 'eighth',
            9: 'ninth',
            10: 'tenth',
            11: 'eleventh',
            12: 'twelfth'
        }
        self.__gifts_counter_dict = {
            2: 'Two ',
            3: 'Three ',
            4: 'Four ',
            5: 'Five ',
            6: 'Six ',
            7: 'Seven ',
            8: 'Eight ',
            9: 'Nine ',
            10: 'Ten ',
            11: 'Eleven ',
            12: 'Twelve '
        }
        self.__gifts_dict = {
            2: 'turtle doves',
            3: 'french hens',
            4: 'calling birds',
            5: 'golden rings',
            6: 'geese a laying',
            7: 'swans a swimming',
            8: 'maids a milking',
            9: 'ladies dancing',
            10: 'lords a leaping',
            11: 'pipers piping',
            12: 'drummers drumming',
        }
        self.__default_song_part = self.get_first_part()

    def get_first_part(self) -> list:
        return [
            f'On the {self.__days_dict.get(1)} day of Christmas',
            self.__second_const_string,
            self.__last_const_string
        ]

    def create_song_part(self, day: int):
        self.__default_song_part.insert(
            day,
            self.__gifts_counter_dict.get(day) + self.__gifts_dict.get(day)
        )

    def show_song_part(self):
        for string in self.__default_song_part:
            print(string)
        print('\n')

    def create_full_song(self):
        self.__default_song_part = self.get_first_part()
        self.show_song_part()
        for day in range(2, 13):
            self.create_song_part(day)
            self.show_song_part()

    def get_song_part(self, day: int):
        if day > 12 or day < 1:
            print('Wrong day number')
        elif day == 1:
            self.__default_song_part = self.get_first_part()
            self.show_song_part()
        else:
            self.__default_song_part = self.get_first_part()

            for day in range(2, day + 1):
                self.create_song_part(day)
            self.show_song_part()

    def get_result(self):
        action = 0
        while action < 1 or action > 2:
            action = int(input('What are u want to do?\n'
                               '1 - Show part of song\n'
                               '2 - Show all song\n'))

        if action == 1:
            day = int(input('Enter day number (between 1 and 12 please):\n'))
            while day < 1 or day > 12:
                day = int(input('Try again please'))

            self.get_song_part(day)
        else:
            self.create_full_song()

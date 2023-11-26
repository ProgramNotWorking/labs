from first_variant import first_task as scrabble
from first_variant import second_task as song
from second_variant import first_task as email
from second_variant import second_task as correction
from third_variant import first_task as shop


class TasksLib:

    @staticmethod
    def get_first_var_first_task():
        return scrabble.Scrabble()

    @staticmethod
    def get_first_var_second_task():
        return song.Song()

    @staticmethod
    def get_second_var_first_task():
        return email.Email()

    @staticmethod
    def get_second_var_second_task():
        return correction.Correction()

    @staticmethod
    def get_third_var_first_task():
        return shop.Shop()

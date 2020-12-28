import random
from pathlib import Path
from colorama import Fore, Back, Style


def hangman():
    """
    The successful game hangman on the Python version
    x Red when a character is invalid
    :return: none
    """
    old_letters_guessed_list = set()

    HANGMAN_ASCII_ART = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
    MAX_TRIES = "מספר נסיונות כושלים - 6"  # random.randint(5 , 10)

    print(HANGMAN_ASCII_ART, "\n", MAX_TRIES)

    # secret_word = input("Please enter a word: ")
    # print("\n" * 14)

    def choose_word(file_path, index):
        """
    The function get file_path:A string (file_path) that represents
     a path to the text file.
    and integer (index) that represents the location of a particular
     word in a file
    The function returns a tuple consisting of
     two members in the following order:
    The number of different words in the file,
     that is, does not include repetitive words.
    A word in a position obtained as an argument to a function (index),
    which will be used as the secret word for guessing
        :param file_path:A string (file_path) that represents a
         path to the text file.
        :type: str
        :param index:An integer (index) that represents the
         location of a particular word in a file
        :type: int
        :return:The function returns a tuple consisting of
         two members in the following order:

        The number of different words in the file,
         that is, does not include repetitive words.
        A word in a position obtained as an argument to a function (index),
        which will be used as the secret word for guessing
        :rtype: tuple
        """
        my_file = Path(file_path)
        my_file_txt = Path(file_path + ".txt")
        if my_file.is_file():
            hangman_words = open(file_path, "r")
            hangman_words_read = hangman_words.read()
            hangman_words_list = hangman_words_read.split(" ")
            hangman_words_set = set()
            for word in hangman_words_list:
                hangman_words_set.add(word)

            hangman_words_set_len = len(hangman_words_set)
            hangman_words_list_len = len(hangman_words_list)
            index_param = index
            while hangman_words_list_len < index_param:
                index_param -= hangman_words_list_len

            choose_word_tuple = (hangman_words_set_len,
                                 hangman_words_list[index_param - 1])
            return choose_word_tuple
        elif my_file_txt.is_file():
            hangman_words = open(my_file_txt, "r")
            hangman_words_read = hangman_words.read()
            hangman_words_list = hangman_words_read.split(" ")
            hangman_words_set = set()
            for word in hangman_words_list:
                hangman_words_set.add(word)

            hangman_words_set_len = len(hangman_words_set)
            hangman_words_list_len = len(hangman_words_list)
            index_param = index
            while hangman_words_list_len < index_param:
                index_param -= hangman_words_list_len

            choose_word_tuple = (hangman_words_set_len,
                                 hangman_words_list[index_param - 1])
            return choose_word_tuple
        else:
            open(file_path, "r")

    def choose_file():
        """
        The function receives from the user a path to an index file and
         removes the secret word from it
        :return: choose_tuple: tuple prepares the secret word and
         its location in the selected file
        :rtype: tuple
        """
        Word_file_input = input(
            "Enter file path(hangman_names/covid/spider3d.txt): ")
        Location_for_word_in_file_input = input("Enter index: ")
        Location_for_word_in_file_input_int = \
            int(Location_for_word_in_file_input)
        choose_tuple = choose_word(Word_file_input,
                                   Location_for_word_in_file_input_int)
        return choose_tuple

    def Preparations_for_the_game():
        """The function decides what the secret word is"""
        global secret_word
        tuple_ward = choose_file()
        secret_word = tuple_ward[1]
        return secret_word.lower()

    secret_word_lower = Preparations_for_the_game()
    print("Let’s start!")
    print("\n")

    def print_hangman(num_of_tries):
        """
    Gets the number of failed guess attempts
    And prints a man depending on the appropriate level
        :param num_of_tries: Gets the number of failed guess attempts
        :return: none
        """
        HANGMAN_PHOTOS = {1: """    x-------x""", 2: """    x-------x
    |
    |
    |
    |
    |
     """, 3: """    x-------x
    |       |
    |       0
    |
    |
    |
     """, 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |
     """, 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |

     """, 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |

     """, 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
     """, 0: ""}
        print(HANGMAN_PHOTOS[num_of_tries])

    print_hangman(1)

    SECRET_WORD_LEN = len(secret_word_lower)

    print("_ " * SECRET_WORD_LEN)

    def show_hidden_word(secret_word_hidden, old_letters_guessed):
        """ Receives the secret word and all the guesses that were up to and
         created STR that each letter that was
        guessed is written and each one of its is marked with '_'
        :param secret_word_hidden: The actor's secret word to guess
        :type: str
        :param old_letters_guessed: A set of all the letters the player
         has already guessed
        :type: set
        :return: show_word: str The guessed letters Addresses and the
         guessed letters are marked with '_'
        :rtype: str
        """
        show_word_lines = "".join([letter + " "
                                   if letter in old_letters_guessed else "_ "
                                   for letter in secret_word_hidden])
        return show_word_lines

    def check_valid_input(letter_guessed, old_letters_guessed):
        """This function Checks if the received character is correct
                :param letter_guessed: user guessed
                 :type letter_guessed: str
                 :param old_letters_guessed: list has save all the old guessed
                 :type old_letters_guessed: set
                 :return: none  """
        letter_guessed_and_old_letters = set()
        if old_letters_guessed == set():
            letter_guessed_and_old_letters = set(letter_guessed)
        else:
            for lett in old_letters_guessed:
                letter_guessed_and_old_letters.add(lett)
            letter_guessed_and_old_letters.add(letter_guessed)

        letter_guessed_and_old_letters_to_print = \
            letter_guessed_and_old_letters.copy()
        for letter in letter_guessed_and_old_letters:
            if letter in secret_word:
                letter_guessed_and_old_letters_to_print.remove(letter)
            else:
                pass

        def isEnglish(english_letter):
            """
            Checks if english letter is an English letter
            :param english_letter: A character who will
             check if it is an English letter
            :type: str
            :return: Whether the character is an English letter or not
            :rtype: int
            """
            try:
                english_letter.encode(encoding='utf-8').decode('ascii')
            except UnicodeDecodeError:
                return 0
            else:
                return 1

        if not letter_guessed.isalpha() and len(letter_guessed) != 1:
            letter_guess_checker = 0
            print(Style.BRIGHT, Fore.RED + 'X', Style.RESET_ALL)
            # print(" -> ".join(sorted(
            # letter_guessed_and_old_letters_to_print)))

        elif not letter_guessed.isalpha():
            letter_guess_checker = 0
            print(Style.BRIGHT, Fore.RED + 'X', Style.RESET_ALL)
            # print(" -> ".join(sorted(
            # letter_guessed_and_old_letters_to_print)))

        elif len(letter_guessed) != 1:
            letter_guess_checker = 0
            print(Style.BRIGHT, Fore.RED + 'X', Style.RESET_ALL)
            # print(" -> ".join(sorted(
            # letter_guessed_and_old_letters_to_print)))

        elif isEnglish(letter_guessed) == 0:
            letter_guess_checker = 0
            print(Style.BRIGHT, Fore.RED + 'X', Style.RESET_ALL)
            # print(" -> ".join(sorted(
            # letter_guessed_and_old_letters_to_print)))

        elif letter_guessed in old_letters_guessed:
            letter_guess_checker = 0
            # print(Style.BRIGHT)
            print(Style.BRIGHT, Fore.RED + 'X', Style.RESET_ALL)
            # print(Style.RESET_ALL)
            # print(" -> ".join(sorted(
            # letter_guessed_and_old_letters_to_print)))

        else:
            letter_guess_checker = 1
        return letter_guess_checker

    def try_update_letter_guessed(letter_guessed,
                                  old_letters_guessed, secret_word_to_update):
        """This function Checks if the received character is correct
                :param letter_guessed: user guessed
                 :type letter_guessed: str
                 :param old_letters_guessed: list has save all the old guessed
                 :type old_letters_guessed: set
                 :param secret_word_to_update: The secret word
                 :type: str
                 :return: Whether the character is correct or not
                 :rtype: bool  """
        letter_guessed_and_old_letters = set()
        if old_letters_guessed == set():
            letter_guessed_and_old_letters = set(letter_guessed)
        else:
            for letter in old_letters_guessed:
                letter_guessed_and_old_letters.add(letter)
            letter_guessed_and_old_letters.add(letter_guessed)

        letter_guessed_and_old_letters_to_print = \
            letter_guessed_and_old_letters.copy()
        for letter_1 in letter_guessed_and_old_letters:
            if letter_1 in secret_word_to_update:
                letter_guessed_and_old_letters_to_print.remove(letter_1)
            else:
                pass

        # check_valid_input(letter_guessed, old_letters_guessed)

        if check_valid_input(letter_guessed, old_letters_guessed) == 0:
            letter_guess_checker = 2
        else:
            if letter_guessed not in secret_word_to_update:
                letter_guess_checker = 0
                print(":(")
                print(" -> ".join(
                    sorted(letter_guessed_and_old_letters_to_print)))

            else:
                letter_guess_checker = 1
                # print(bool(letter_guess_checker))

        return letter_guess_checker

    def check_win(secret_word_to_check_win, old_letters_guessed):
        """checker if player wins or not
        :param secret_word_to_check_win: The actor's secret word to guess
        :type: str
        :param old_letters_guessed: A set of all the letters
         the player has already guessed
        :type: set
        :return: check_win_bool:
        :rtype: bool
        """
        check_win_len = 0
        for letter in secret_word_to_check_win:
            if letter in old_letters_guessed:
                check_win_len += 1
            else:
                pass
        if check_win_len == len(secret_word_to_check_win):
            check_win_bool = 1
        else:
            check_win_bool = 0
        return bool(check_win_bool)

    def progress_of_the_game():
        failed_attempts = 0
        while failed_attempts < 6:  # 7
            user_letter_first_guess_input = input("Guess a letter: ")
            user_letter_first_guess = user_letter_first_guess_input.lower()

            update_letter_guessed = try_update_letter_guessed(
                user_letter_first_guess,
                old_letters_guessed_list,
                secret_word_lower)
            if update_letter_guessed == 0:
                old_letters_guessed_list.add(user_letter_first_guess)
                failed_attempts += 1
                failed_attempts_1 = failed_attempts + 1
                print_hangman(failed_attempts_1)
                print(show_hidden_word(secret_word_lower,
                                       old_letters_guessed_list))
            elif update_letter_guessed == 2:
                print(show_hidden_word(secret_word_lower,
                                       old_letters_guessed_list))

            else:
                old_letters_guessed_list.add(user_letter_first_guess)
                failed_attempts_1 = failed_attempts + 1
                print_hangman(failed_attempts_1)
                print(show_hidden_word(secret_word_lower,
                                       old_letters_guessed_list))

            if check_win(secret_word_lower, old_letters_guessed_list):
                # print("כל הכבוד ניצחת!")
                print("WIN")
                break
            if failed_attempts == 6:
                # print("game over")
                print("LOSE")

    progress_of_the_game()


def main():
    hangman()
    # Call the function func


if __name__ == "__main__":
    main()

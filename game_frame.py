#############################################################
# FILE: ex12_utils.py
# WRITERS: 1.Amir Rosengarten, amir.rosen15, 207942285,
# 2. Avital Harel, avital.harel, 211743381
# EXERCISE: intro2cs2 ex12 2022
# DESCRIPTION:In this exercise we implement a version of the "boggle"
# game.
# In this file, we implement the auxiliary functions.
#############################################################

import tkinter as tk
from ex12_utils import *
from boggle_board_randomizer import *
from button import LetterButton

GAME_TIME = 180


class GameFrame(tk.Frame):
    """
    a frame of the game
    """

    def __init__(self, root, gm):
        super().__init__(root)
        self.gm = gm
        self.word_lst = []
        self.read_words_from_file('boggle_dict.txt')
        self.current_pressed_buttons = []
        self.board_game = randomize_board()  # 2D list of letters
        self.length = len(self.board_game)
        self.width = len(self.board_game[0])

        self.current_words = self.word_lst[:]  # words that weren't found
                                            # yet
        self.score = 0
        self.letter_button_lst = []  # list of all the button objects that
                                    # are letters on the board
        self.letters_frame = tk.Frame(self)
        self.submit_button = None
        self.time_left = GAME_TIME
        self.timer_label = None

        self.current_clicked_letters = ""  # all the letters the player
                                # clicked on before clicking of submit


        self.current_clicked_letters_label = None
        self.found_words = []
        self.found_words_label = None

        self.exit_game_button = None
        self.init_game()

        self.grid_all_objects()



    def read_words_from_file(self, filename='boggle_dict.txt'):
        """
        reads the word file and adds the words to a list
        :param filename: file
        """
        with open(filename, "r") as f:
            word_list = f.readlines()

        for word in word_list:
            word = word.strip("\n")
            self.word_lst.append(word)

    def init_game(self):
        """
        creates all the buttons and labels that are in the game
        """
        for i in range(self.width):
            self.letter_button_lst.append([])
            for j in range(self.length):
                button_object = LetterButton((i, j), self.board_game[i][j],
                                             self.letters_frame)

                button_tk_object = LetterButton.get_button(button_object)

                button_tk_object.config(
                    command=self.clicked_button(self.board_game[i][j],
                                                (i, j)))
                self.letter_button_lst[i].append(button_object)
                self.letter_button_lst[i][j].get_button()\
                    .grid(row=i, column=j)

        self.submit_button = tk.Button(self, text="sumbit", bg="black",
                                       fg="white", bd=10,
                                       font=("Helvetica", 20),
                                       command=self.update_submit)
        self.score_label = tk.Label(self, text="score: 0",
                                    font=("Cooper Black", 30))
        self.found_words_label = tk.Label(self, text="", fg="black",
                                          font=("Cooper Black", 14))
        self.timer_label = tk.Label(self, fg="black",
                                    font=("Cooper Black", 20))
        self.exit_game_button = tk.Button(self,
                                          text="exit game",
                                          bg="white",
                                          fg="grey",
                                          font=("Cooper Black", 15),
                                          command=self.gm.get_root()
                                          .destroy)
        self.reset_game_button = tk.Button(self,
                                          text="reset game",
                                          bg="white",
                                          fg="grey",
                                          font=("Cooper Black", 15),
                                          command=self.gm.reset_game)
        self.current_clicked_letters_label = tk.Label(self, text="",
                                                      fg="grey",
                                                      font=(
                                                          "Cooper Black",
                                                          20))

    def update_score(self, score):
        """
        updates players score in the given value
        :param score: int,score
        """
        self.score_label["text"] = f"score: {score}"

    def update_submit(self):
        """
        all the things that happen after the player clicked on submit
         button
        """
        res = is_valid_path(self.board_game,
                            self.current_pressed_buttons,
                            self.current_words)
        if res is not None and res in self.current_words:
            n = len(self.current_pressed_buttons)
            self.score += n * n
            self.update_score(self.score)
            self.found_words.append(res)
            self.found_words_label['text'] = self.found_words
            self.current_words.remove(res)
        self.current_pressed_buttons = []
        self.current_clicked_letters = ""
        self.current_clicked_letters_label['text'] = ""

    def clicked_button(self, letter, location):
        """
        all the things that happen after the player clicked on a button
        :param letter: str, the value of the button
        :param location: tuple, the location on the board of the button
        :return:
        """

        def clicked():
            self.current_clicked_letters += letter
            self.current_clicked_letters_label[
                'text'] = self.current_clicked_letters
            self.current_pressed_buttons.append(location)

        return clicked

    def countdown(self):
        """
        a clock
        """
        sec = str(self.time_left % 60)
        while len(sec) <= 1:
            sec = '0' + sec
        min = str(self.time_left // 60)
        while len(min) <= 1:
            min = '0' + min
        self.timer_label['text'] = f' remaining time: {min}:{sec}'
        if self.time_left > 0:
            self.after(1000, self.countdown)
            self.time_left = self.time_left - 1
        else:
            self.gm.create_final_frame()




    def grid_all_objects(self):
        """
        place all objects using grid
        """
        self.score_label.grid(row=0, column=0)
        self.timer_label.grid(row=1, column=0)
        self.current_clicked_letters_label.grid(row=3, column=0)
        self.letters_frame.grid(row=4, column=0)
        self.found_words_label.grid(row=7, column=0)
        self.submit_button.grid(row=10, column=0)
        self.exit_game_button.grid(row=0, column=2)
        self.reset_game_button.grid(row=0,column=1)

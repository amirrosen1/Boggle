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
from game_frame import GameFrame
from start_game_frame import StartGameFrame
from final_frame import FinalFrame

class GameManager:
    """
    the main class of the boggle game
    """
    def __init__(self):
        root = tk.Tk()
        root.geometry("1200x800")
        root.maxsize(1000, 600)
        root.title("boggle game")
        self.__root = root
        self.starting_window = StartGameFrame(self.__root, self)
        self.game_frame = GameFrame(self.__root, self)
        self.final_frame = FinalFrame(self.__root, self)

    def create_starting_game_window(self):
        """
        creates the first frame that will appear to the player
        """

        self.starting_window.pack()
        self.__root.mainloop()

    def create_game_frame(self):
        """
        creates the actual game
        :return
        """
        self.starting_window.pack_forget()
        self.game_frame.countdown()
        self.game_frame.pack()

    def create_final_frame(self):
        """creates a frame where the player will be asked if he would like
        to play again"""
        self.game_frame.pack_forget()
        self.final_frame.pack()

    def play_again(self):
        self.final_frame.pack_forget()
        self.game_frame = GameFrame(self.__root, self)
        self.game_frame.countdown()
        self.game_frame.pack()

    def reset_game(self):
        self.game_frame.pack_forget()
        self.game_frame = GameFrame(self.__root, self)
        self.game_frame.countdown()
        self.game_frame.pack()

    def get_root(self):
        """
        a getter for the gm root
        :return:
        """
        return self.__root


if __name__ == '__main__':
    g = GameManager()
    g.create_starting_game_window()

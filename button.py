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


class LetterButton:
    """
    creates button object for buttons on the board
    """
    def __init__(self, location, value, frame_parent):
        self.location = location
        self.value = value
        self.frame_parent = frame_parent
        i = location[0]
        j = location[1]
        self.__button = tk.Button(self.frame_parent, text=value, height=1,
                                width=4,bg="black", fg="white", bd=10,
                                font=("Helvetica", 25))

        self.__button.grid(row=i, column=j)


    def get_button(self):
        """
        a getter for the button
        :return:
        """
        return self.__button










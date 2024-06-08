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
from PIL import Image, ImageTk


class StartGameFrame(tk.Frame):

    """
    the frame that appears before the game begins
    """

    def __init__(self, root, gm):
        super().__init__(root)
        self.root = root
        self.gm = gm
        self.canvas = tk.Canvas(self, width=1500, height=1500)

        # Add image file
        img = ImageTk.PhotoImage(
            Image.open('letters.jfif').resize((1000, 600),
                                              Image.ANTIALIAS))

        self.canvas.background = img  # Keep a reference in case this
        # code is put in a function.
        bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # Create Frame
        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)
        self.frame3 = tk.Frame(self)
        self.canvas.create_window(420, 100, anchor=tk.NW,
                                  window=self.frame1)
        self.canvas.create_window(600, 400, anchor=tk.NW,
                                  window=self.frame2)
        self.canvas.create_window(550, 300, anchor=tk.NW,
                                  window=self.frame3)
        self.start_game_button = tk.Button(self.frame3, fg="white",
                                           bg="black",
                                           height=1,
                                           width=15,
                                           text="lets start the game",
                                           font=("Jokerman", 25),
                                           command=gm.create_game_frame)

        self.end_game_button = tk.Button(self.frame2, fg="white",
                                         bg="black",
                                         height=1,
                                         width=15,
                                         text='END THE GAME',
                                         font=("Jokerman", 15),
                                         command=gm.get_root().destroy)

        self.game_name_label = tk.Label(self.frame1, fg="white",
                                        bg="black",
                                        height=1,
                                        width=15,
                                        text="boggle game",
                                        font=("Jokerman", 50))
        self.grid_all_objects()

    def grid_all_objects(self):
        self.canvas.grid(row=0, column=0)
        self.start_game_button.grid(row=20, column=80)
        self.end_game_button.grid(row=10, column=0)
        self.game_name_label.grid(row=8, column=80)

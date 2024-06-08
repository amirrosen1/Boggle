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


class FinalFrame(tk.Frame):
    """
    creates the frame after the time of the game is finished
    asking the user if he would like to play again
    """
    def __init__(self, root,gm):
        super().__init__(root)
        self.root = root
        self.gm = gm
        self.play_again_label = tk.Label(self, bg="black", fg="white",
                                         height=1,
                                         width=15,
                                         text="play again?",
                                         font=("Cooper Black", 100))

        self.exit_game_button = tk.Button(self,
                                         text="exit game",
                                         fg="grey",
                                         font=("Cooper Black", 20),
                                          command=gm.get_root().destroy)
        self.play_again_button = tk.Button(self,
                                         text="play again",
                                         fg="grey",
                                         font=("Cooper Black", 20)
                                           ,command=gm.play_again)
        self.pack_all_objects()



    def pack_all_objects(self):
        """
        placing all the buttons and labels in the frame
        """
        self.play_again_button.pack(side=tk.BOTTOM)
        self.exit_game_button.pack(side=tk.BOTTOM)
        self.play_again_label.pack(side=tk.TOP)

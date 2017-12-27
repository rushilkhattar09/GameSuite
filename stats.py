from Tkinter import *

class Score:
    def __init__ (self):
        self.game = str()
        self.user = str()
        self.level = str()
        self.score = str()

    def read_str (self, string):
        string = string.split(',')
        self.game, self.user, self.level, self.score = string
        return None

    def label (self, r):
        Label(root, text = self.game, \
            fg = "Cadet Blue", font = "Helvetica", \
            width = 24).grid(row = r, column = 0)
        Label(root, text = self.user, \
            fg = "Cadet Blue", font = "Helvetica", \
            width = 12).grid(row = r, column = 1)
        Label(root, text = self.level, \
            fg = "Cadet Blue", font = "Helvetica", \
            width = 4).grid(row = r, column = 2)
        Label(root, text = self.score, \
            fg = "Cadet Blue", font = "Helvetica", \
            width = 8).grid(row = r, column = 3)

    def __str__ (self):
        string = self.game, self.user, self.level, self.score
        return ','.join(string)

stat_list = list()

def read_stats ():
    with open("scores.txt") as f:
        for a in f.readlines():
            stat_list.append(Score())
            stat_list[-1].read_str(a.strip('\n'))

def show_stats ():
    for a, b in enumerate(stat_list):
        b.label(a)

root = Tk()
root.title(string = "Game Stats")

read_stats()
show_stats()

root.mainloop()

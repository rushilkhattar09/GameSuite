import os
from Tkinter import *

with open("game_list.txt") as f:
    games = f.readlines()

game_path = list(games)
for a in xrange(len(games)):
    games[a] = games[a].strip('\n')
    game_path[a] = games[a]+'/Python/tkinter-gui.py'

# print "Choose your game"
# for a, b in enumerate(games):
#     print "%d : %s" % (a, b)
#
# for a in xrange(len(games)):
# 	print a, ":", games[a]

back = "Mint Cream"

root = Tk()
root.title(string = "Game Suite")
root.config(bg = back)

Label(root, text = "Choose Your Game",
      font = "Georgia 24", bg = back,
      fg = "Crimson", width = "20").pack()

print games
print game_path

def f (event):
    game = event.widget
    game = game.cget('text')
    game = games.index(game)
    root.destroy()
    os.system("clear")
    os.system("python " + game_path[game])

g = list()
for a, b in enumerate(games):
    print a,b
    c = Button(root, text = b, height = 2, \
        font = "Arial 12", relief = FLAT, \
        fg = "Royal Blue", width = "48", bg = back)
    c.bind("<1>", f)
    c.pack()
    g.append(c)

root.mainloop()

"""
# Game_list #
Minesweeper
Rullo
Connect4
"""

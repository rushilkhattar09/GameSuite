sizes = [5, 6, 7, 8]
connects = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

print "Choose your battleground"
for a,b in enumerate(sizes):
    print "%d : %d * %d" % (a, b, b)
# board = sizes[int(raw_input())]
board = int(raw_input())

table = [[' ' for a in xrange(board)] for b in xrange(board)]

def display():
    for a in xrange(board):
        print '.....'*board
        print ':', ' :: '.join(table[a]), ':'
        print '.....'*board

players = 0

def Valid(point):
    if (point[0] in range(board)) and (point[1] in range(board)):
        return 1
    return 0

def check_4(point):
    x, y = point
    colour = table[x][y]
    # print table
    """
    Combo map
    7 0 1
    6 0 2
    5 4 3
    """

    for i in connects:
        x1 = int(x)
        y1 = int(y)
        check_points = list()
        for f in xrange(4):
            if Valid([x1,y1]):
                check_points.append(table[x1][y1])
            # print x1,y1
            x1 = x1+i[0]
            y1 = y1+i[1]
        # print check_points, i
        if len(filter(lambda x : x == colour, check_points)) == 4:
            # print "WON"
            return True
    return False

print "Starts from col 0"
display()
dropped = 0
won = False
while not won and dropped != board**2:
    drop = raw_input()
    if not drop:
        continue
    drop = int(drop)
    if drop not in range(board):
        continue
    for a in xrange(board-1, -1, -1):
        if table[a][drop] == ' ':
            dropped += 1
            table[a][drop] = str(players)
            players = int(not players)
            won = check_4([a,drop])
            break
    display()
if won:
    print "You WON!!"

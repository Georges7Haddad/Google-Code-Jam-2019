""" The commented program is enough to answer the problem by reverting Lydia's path.
The following program is used to show what move is made by the user and by Lydia at every position.
It shows that the user does not reuse any of Lydia's moves.
"""


'''
path = []
for move in P:
    if move == 'E':
        path.append('S')
    if move == 'S':
        path.append('E')
print(path)
'''

T = int(input("Please enter T: "))
for i in range(T):
    N = int(input("Enter maze size: "))
    P = input("Enter Lydia's Path: ")

    LydiaMoves = {}
    UserMoves = {}
    xPosition = 0
    yPosition = 0

    for move in P:
        if move == 'E':
            LydiaMoves[str(xPosition) + str(yPosition)] = move
            UserMoves[str(yPosition) + str(xPosition)] = 'S'
            xPosition = xPosition + 1
        if move == 'S':
            LydiaMoves[str(xPosition) + str(yPosition)] = move
            UserMoves[str(yPosition) + str(xPosition)] = 'E'
            yPosition = yPosition + 1
    path = ""
    print("Case", i, ":", path.join(UserMoves.values()))


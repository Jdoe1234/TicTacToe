import time
import random

def TicTacToe():
    time.sleep(0.2)
    print('')
    time.sleep(0.2)
    print('welcome to TicTacToe')
    time.sleep(0.2)
    print('')
    time.sleep(0.2)
    print('You be X and I\'ll be O')
    main()

def main():
    global board
    board = ['#'] * 9
    
    time.sleep(0.2)
    val = input('Do You want to go "first" or "second?": ')
    if val == 'first':
        time.sleep(0.2)
        Help()
        time.sleep(0.2)
        print('')
        time.sleep(0.2)
        PlayerChoice()
    elif val == 'second':
        time.sleep(0.2)
        print('Then I will go first')
        time.sleep(1)
        print('Placing in the middle ofcourse ;)')
        ComputerChoice()
    else:
        val = input('Please enter either "first" or "second": ')
        main(val)

def UnavailableTile():
    time.sleep(0.2)
    print('Tile is already taken')
    time.sleep(0.2)
    print('please pick anoter tile')
    time.sleep(0.2)
    print('')
    BoardUpdate()
    PlayerChoice()

def Help():
    time.sleep(0.2)
    print('When choosing a tile, pick between:')
    time.sleep(0.2)
    print('')
    time.sleep(0.2)
    print('  nw, n, ne')
    time.sleep(0.2)
    print('  w , m, e ')
    time.sleep(0.2)
    print('  sw, s, se')
    time.sleep(0.2)
    print('')
    PlayerChoice()


def PlayerChoice():
    time.sleep(0.2)
    val = input('Please choose a Tile: ')
    tilerange = ['nw', 'n', 'ne', 'w', 'm', 'e', 'sw', 's', 'se']

    for i in range(len(tilerange)):
        if val == tilerange[i] and board[i] == '#':
            board[i] = 'X'
        elif val == tilerange[i] and board[i] != '#':
            UnavailableTile()
    
    if tilerange.count(val) != 1:
        Help()
    
    BoardUpdate()
    ComputerChoice()
    BoardUpdate()
    PlayerChoice()


def BoardUpdate():
    lines = [board[:3], board[3:6], board[6:], [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]], [board[0], board[4], board[8]], [board[2], board[4], board[6]]]
    time.sleep(0.2)
    print('')
    time.sleep(0.2)
    print('  ' + board[0], board[1], board[2])
    time.sleep(0.2)
    print('  ' + board[3], board[4], board[5])
    time.sleep(0.2)
    print('  ' + board[6], board[7], board[8])
    time.sleep(0.2)
    print('')

    for i in range(len(lines)):
        if lines[i].count('O') == 3:
            print('I have Won')
            End()
        elif lines[i].count('X') == 3:
            print('You have Won')
            End()
    if board.count('#') == 0:
        time.sleep(0.2)
        print('')
        time.sleep(0.2)
        print('there are no winners')
        End()

def End():
    time.sleep(0.2)
    print('The Game is over')
    time.sleep(0.2)
    print('')
    time.sleep(0.2)
    input('Press enter to try again')
    time.sleep(0.2)
    print('')
    main()


def ComputerChoice():
    time.sleep(0.2)
    print('My turn!')
    lines = [board[:3], board[3:6], board[6:], [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]], [board[0], board[4], board[8]], [board[2], board[4], board[6]]]

    DetectOLoop(lines)
    DetectXLoop(lines)
    PriorityPick()

def DetectOLoop(lines):
    for i in range(len(lines)):
        #detect 2 O's
        if lines[i].count('O') == 2 and lines[i].count('#') == 1:
            #if found, look for avalable tile, else start next priority loop
            htag = lines[i].index('#')
            lines[i][htag] = 'O'
            overwrite(lines[i], i)

def DetectXLoop(lines):
    for i in range(len(lines)):
        if lines[i].count('X') == 2 and lines[i].count('#') == 1:
            #if found, look for avalable tile, else start next priority loop
            htag = lines[i].index('#')
            currentLine = lines[i]
            currentLine[htag] = 'O'
            overwrite(lines[i], i)

def PriorityPick():
    if board[4] == '#':
        board[4] = 'O'
    elif board[0] == '#':
        board[0] = 'O'
    elif board[2] == '#':
        board[2] = 'O'
    elif board[6] == '#':
        board[6] = 'O'
    elif board[8] == '#':
        board[8] = 'O'
    elif board[1] == '#':
        board[1] = 'O'
    elif board[3] == '#':
        board[3] = 'O'
    elif board[5] == '#':
        board[5] = 'O'
    elif board[7] == '#':
        board[7] = 'O'               

def overwrite(oline, olinenr):
    if olinenr == 0:
        board[0] = oline[0]
        board[1] = oline[1]
        board[2] = oline[2]
    elif olinenr == 1:
        board[3] = oline[0]
        board[4] = oline[1]
        board[5] = oline[2]
    elif olinenr == 2:
        board[6] = oline[0]
        board[7] = oline[1]
        board[8] = oline[2]
    elif olinenr == 3:
        board[0] = oline[0]
        board[3] = oline[0]
        board[6] = oline[2]
    elif olinenr == 4:
        board[1] = oline[0]
        board[4] = oline[1]
        board[7] = oline[2]
    elif olinenr == 5:
        board[2] = oline[0]
        board[5] = oline[1]
        board[8] = oline[2]
    elif olinenr == 6:
        board[0] = oline[0]
        board[4] = oline[1]
        board[8] = oline[2]
    elif olinenr == 7:
        board[2] = oline[0]
        board[4] = oline[1]
        board[6] = oline[2]

    BoardUpdate()
    PlayerChoice()


def RandomPick():
    if board[4] == '#':
        board[4] = 'O'
    else:
        val = random.randint(0, 9)
        if board[val] =='#':
            board[val] = 'O'
            BoardUpdate()
            PlayerChoice()
        else:
            RandomPick

TicTacToe()
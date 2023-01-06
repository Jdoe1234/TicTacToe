import time
import PySimpleGUI as sg

global board
board = [' '] * 9
roundsCounter = -1


def ComputerChoice():
    time.sleep(0.2)
    print('My turn!')
    lines = [board[:3], board[3:6], board[6:], [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]], [board[0], board[4], board[8]], [board[2], board[4], board[6]]]

    action = 0

    #detect O's
    if action == 0:
        for i in range(len(lines)):
            if lines[i].count('O') == 2 and lines[i].count(' ') == 1:
                #if found, look for avalable tile, else start next priority loop
                htag = lines[i].index(' ')
                lines[i][htag] = 'O'
                overwrite(lines[i], i)
                action =+ 1
                lines.clear()
                break

    #detect 2 X's
    if action == 0:
        for i in range(len(lines)):
            if lines[i].count('X') == 2 and lines[i].count(' ') == 1:
                #if found, look for avalable tile, else start next priority loop
                htag = lines[i].index(' ')
                currentLine = lines[i]
                currentLine[htag] = 'O'
                overwrite(lines[i], i)
                lines.clear()
                action =+ 1
                break

    if action == 0:
        if board[4] == ' ':
            board[4] = 'O'
        elif board[0] == ' ':
            board[0] = 'O'
        elif board[2] == ' ':
            board[2] = 'O'
        elif board[6] == ' ':
            board[6] = 'O'
        elif board[8] == ' ':
            board[8] = 'O'
        elif board[1] == ' ':
            board[1] = 'O'
        elif board[3] == ' ':
            board[3] = 'O'
        elif board[5] == ' ':
            board[5] = 'O'
        elif board[7] == ' ':
            board[7] = 'O'
    lines.clear()
       

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


def main(clickinput):
    if clickinput == 9 and roundsCounter >=1:
        print('Then I will go first')
        ComputerChoice()
        BoardUpdate()
        window['-MESSAGEBUTTON-'].update(visible=False)
        window['-MESSAGE-'].update('Then I will go first')
        return
                
    if clickinput == 9 and roundsCounter >= 1:
        window['-MESSAGEBUTTON-'].update('Second', visible=False)
        window['-MESSAGE-'].update('It is Your turn')
    
    elif clickinput == 10 and roundsCounter == 1:
        ComputerChoice()
        BoardUpdate()
        return

    if clickinput < 9:
        for i in range(len(board)):
            board[clickinput] = 'X'
    

# fix later   
    lines = [board[:3], board[3:6], board[6:], [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]], [board[0], board[4], board[8]], [board[2], board[4], board[6]]]
    print('')
    print('  ' + board[0], board[1], board[2])
    print('  ' + board[3], board[4], board[5])
    print('  ' + board[6], board[7], board[8])
    print('')

    for i in range(len(lines)):
        if lines[i].count('O') == 3:
            print('I have Won')
            sg.popup_ok('I Have Won')
            lines.clear()
            for i in range(len(board)):
                x = '-TILE' + str(i) + '-'
                window[x].update(board[i])
            return

        elif lines[i].count('X') == 3:
            print('You have Won')
            sg.popup_ok('You Have Won')
            lines.clear()
            for i in range(len(board)):
                x = '-TILE' + str(i) + '-'
                window[x].update(board[i])
            return

    if board.count(' ') == 0:
        print('there are no winners')
        sg.popup_ok('there are no winners')
        lines.clear()
        return

    
    for i in range(len(board)):
        x = '-TILE' + str(i) + '-'
        window[x].update(board[i])
# fix later

    if roundsCounter > 0 or clickinput == 9:
        ComputerChoice()
        BoardUpdate()

   
        


def BoardUpdate():
    lines = [board[:3], board[3:6], board[6:], [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]], [board[0], board[4], board[8]], [board[2], board[4], board[6]]]
    print('')
    print('  ' + board[0], board[1], board[2])
    print('  ' + board[3], board[4], board[5])
    print('  ' + board[6], board[7], board[8])
    print('')

    for i in range(len(lines)):
        if lines[i].count('O') == 3:
            print('I have Won')
            sg.popup_ok('I Have Won')
            lines.clear()
            for i in range(len(board)):
                x = '-TILE' + str(i) + '-'
                window[x].update(board[i])
            return

        elif lines[i].count('X') == 3:
            print('You have Won')
            sg.popup_ok('You Have Won')
            lines.clear()
            for i in range(len(board)):
                x = '-TILE' + str(i) + '-'
                window[x].update(board[i])
            return

    if board.count(' ') == 0:
        print('there are no winners')
        sg.popup_ok('there are no winners')
        lines.clear()
    
    for i in range(len(board)):
        x = '-TILE' + str(i) + '-'
        window[x].update(board[i])


sg.theme('Dark Blue 2')

layout = [
    [sg.Text('TicTacToe'), sg.Button('exit', key='Exit', button_color=('red'))],
    [sg.Button(board[0], key= '-TILE0-', size=(2, 1), visible=False), sg.Button(board[1], key= '-TILE1-', size=(2, 1), visible=False), sg.Button(board[2], key= '-TILE2-', size=(2, 1), visible=False)],
    [sg.Button(board[3], key= '-TILE3-', size=(2, 1), visible=False), sg.Button(board[4], key= '-TILE4-', size=(2, 1), visible=False), sg.Button(board[5], key= '-TILE5-', size=(2, 1), visible=False)],
    [sg.Button(board[6], key= '-TILE6-', size=(2, 1), visible=False), sg.Button(board[7], key= '-TILE7-', size=(2, 1), visible=False), sg.Button(board[8], key= '-TILE8-', size=(2, 1), visible=False)],
    [sg.Text('Hi, Welcome to TicTacToe!', key='-MESSAGE-')],
    [sg.Button('Go Again!', visible=False, key= '-MESSAGEBUTTON2-'), sg.Button('Start', visible=True, key= '-MESSAGEBUTTON-')]
]

window = sg.Window('TicTacToe', layout, grab_anywhere = True, no_titlebar = True)


while True:
    roundsCounter += 1
    print(roundsCounter, '-------------------')
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

        
    if roundsCounter == 0:
        window['-MESSAGEBUTTON-'].update('Second', visible=True)
        window['-MESSAGE-'].update('Choose a Tile or press the "Second" button')
        window['-MESSAGEBUTTON2-'].update('go again', visible=True)
        for i in range(len(board)):
            x = '-TILE' + str(i) + '-'
            window[x].update(visible=True)
        window['-MESSAGE-'].update('if you want to go first, the press a tile, press the "Second" button to let me start!')
    
    if event == '-MESSAGEBUTTON-' and roundsCounter >=1:
        main(9)


    elif event == '-TILE0-' and board[0] == ' ':
        window['-TILE0-'].update(board[0])
        main(0)

    elif event == '-TILE1-' and board[1] == ' ':
        window['-TILE1-'].update(board[1])
        main(1)

    elif event == '-TILE2-' and board[2] == ' ':
        window['-TILE2-'].update(board[2])
        main(2)

    elif event == '-TILE3-' and board[3] == ' ':
        window['-TILE3-'].update(board[3])
        main(3)

    elif event == '-TILE4-' and board[4] == ' ':
        window['-TILE4-'].update(board[4])
        main(4)

    elif event == '-TILE5-' and board[5] == ' ':
        window['-TILE5-'].update(board[5])
        main(5)

    elif event == '-TILE6-' and board[6] == ' ':
        window['-TILE6-'].update(board[6])
        main(6)

    elif event == '-TILE7-' and board[7] == ' ':
        window['-TILE7-'].update(board[7])
        main(7)

    elif event == '-TILE8-' and board[8] == ' ':
        window['-TILE8-'].update(board[8])
        main(8)

    elif event == '-end0-' or event == '-end1-' or event == '-end2-':
        board = [' '] * 9
        roundsCounter = 0
        window['-MESSAGE-'].update('if you want to go first, the press a tile, press the "Second" button to let me start!')
        window['-MESSAGEBUTTON-'].update('Second', visible=True)
        main(10)

    elif event == '-MESSAGEBUTTON2-':
        board = [' '] * 9
        roundsCounter = 0
        window['-MESSAGE-'].update('if you want to go first, the press a tile, press the "Second" button to let me start!')
        window['-MESSAGEBUTTON-'].update('Second', visible=True)
        main(10)

    

window.close()
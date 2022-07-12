from tkinter import Tk, Menu, Button, Label, W
import random
import tkinter.font as font

#Tkinter window settings
window =Tk()
menu = Menu(window)
window.title('TicTacToe')
window.config(menu=menu)
submenu = Menu(menu, tearoff = 0)
window.geometry("300x350")

menu.add_cascade(labe="Menu", menu=submenu)
submenu.add_command(label="Exit", command=window.destroy)

#Game board, with winning options
board = [['','',''],['','',''],['','','']]
count = 0

def winning_combos(x:str) -> None:
    if (board[0][0] == board[0][1] == board[0][2] == x or board[1][0] == board[1][1] == board[1][2] == x or board[2][0] == board[2][1] == board[2][2] == x or
    board[0][0] == board[1][0] == board[2][0] == x or board[0][1] == board[1][1] == board[2][1] == x or board[0][2] == board[1][1] == board[2][2] == x or
    board[0][0] == board[1][1] == board[2][2] == x or board[0][2] == board[1][1] == board[2][0] == x):
        info['text'] = f'Player {x} wins'
        info['fg'] = '#66FFB2'
        return None
    elif count == 9:
        info['text'] = 'Its a tie'

#Functions change button labels and append board list with provided values
def button_changer(button, x:int, y:int):
    global count
    global board
    global list_of_moves 
    if  button['text'] == '':
        if count % 2 == 0:
            button['text'] = 'X'
            button['fg'] = '#FF66B2'
            board[x][y] = 'X'
            count += 1
            label_changer()
            winning_combos('X')
            if info['text'] == 'Player X wins':
                return None
            list_of_moves.remove([button, x, y])
    else:
        return None
    pc_move()
            
def label_changer() -> None:
    global count
    if count % 2 == 0:
        info['text'] = 'Player X turn'
    else:
        info['text'] = 'Player O turn'

def click_midle_button() ->None:
    global count
    global board
    global list_of_moves 
    button5['text'] = 'O'
    button5['fg'] = '#6666FF'
    board[1][1] = 'O'
    count += 1
    label_changer()
    winning_combos('O')
    if info['text'] == 'Player O wins':
        return None
    list_of_moves.remove([button5, 1, 1])

def pc_move() -> None:
    global count
    global board
    global list_of_moves 
    if  button5['text'] == '':
        click_midle_button()
    else:
        random_click = random.choice(list_of_moves)
        button = random_click[0]
        x = random_click[1]
        y = random_click[2]
        button['text'] = 'O'
        button['fg'] = '#6666FF'
        board[x][y] = 'O'
        count += 1
        label_changer()
        winning_combos('O')
        if info['text'] == 'Player O wins':
            return None
        list_of_moves.remove([button, x, y])

#Function to reset the game
def clear_the_board() -> None:
    global board
    global count
    global list_of_moves
    board = [['','',''],['','',''],['','','']]
    button1['text'] = button2['text'] = button3['text'] = button4['text'] = button5['text'] = button6['text'] = button7['text'] = button8['text'] = button9['text'] = ''
    count = 0
    info['text'] = ''
    list_of_moves = [[button1, 0, 0], [button2, 0, 1], [button3, 0, 2], [button4, 1, 0], [button5, 1, 1], [button6, 1, 2], [button7, 2, 0], [button8, 2, 1], [button9, 2, 2]]

submenu.add_command(label="Play again", command=clear_the_board)
         
#Button visuals with commands
helv36 = font.Font(family='Helvetica', size=36, weight='bold')
helv18 = font.Font(family='Helvetica', size=18, weight='bold')
   
button1 = Button(window, text="", fg='black', height= 1, width=3, font=helv36, command=lambda: button_changer(button1, 0, 0))
button2 = Button(window, text="", fg='black', height= 1, width=3, font=helv36, command=lambda: button_changer(button2, 0, 1))
button3 = Button(window, text="", fg='black', height= 1, width=3, font=helv36, command=lambda: button_changer(button3, 0, 2))
button4 = Button(window, text="", fg='black', height= 1, width=3, font=helv36, command=lambda: button_changer(button4, 1, 0))
button5 = Button(window, text="", fg='black', height= 1, width=3, font=helv36, command=lambda: button_changer(button5, 1, 1))
button6 = Button(window, text="", fg='black', height= 1, width=3, font=helv36, command=lambda: button_changer(button6, 1, 2))
button7 = Button(window, text="", fg='black', height= 1, width=3, font=helv36, command=lambda: button_changer(button7, 2, 0))
button8 = Button(window, text="", fg='black', height= 1, width=3, font=helv36, command=lambda: button_changer(button8, 2, 1))
button9 = Button(window, text="", fg='black', height= 1, width=3, font=helv36, command=lambda: button_changer(button9, 2, 2))
info = Label(window, text="Player X turn", fg='black', font=helv18)

#Move of list PC can use
list_of_moves = [[button1, 0, 0], [button2, 0, 1], [button3, 0, 2], [button4, 1, 0], [button5, 1, 1], [button6, 1, 2], [button7, 2, 0], [button8, 2, 1], [button9, 2, 2]]

button1.grid(row=1, column=0, sticky=W)
button2.grid(row=1, column=1, sticky=W)
button3.grid(row=1, column=2, sticky=W)
button4.grid(row=2, column=0, sticky=W)
button5.grid(row=2, column=1, sticky=W)
button6.grid(row=2, column=2, sticky=W)
button7.grid(row=3, column=0, sticky=W)
button8.grid(row=3, column=1, sticky=W)
button9.grid(row=3, column=2, sticky=W)
info.grid(row=4, column =0, columnspan=3, sticky=W)

window.mainloop()
import tkinter as tk
from tkinter import messagebox

# initializing player and board
player = 'X'
board = [['' for j in range(3)] for i in range(3)]

# main window and master
root = tk.Tk()
root.geometry("500x400+720+200")
root.title('Tic Tac Toe')

# function to initiate on click
def on_click(row, col):
    global player, board

    # updating the board and buttons
    if board[row][col] == '':
        board[row][col] = player
        update_buttons(row ,col)

        # checking if the game is won or tied and then resetting the game
        if main_game_logic():
            messagebox.showinfo('Game Over', f'Congratulations Player {player}! You won.')
            reset()
        elif no_more_moves():
            messagebox.showinfo('Game Over', 'No more moves possible, the game is tied.')
            reset()
        else:
            switch()

# updating buttons with 'X' or 'O'
def update_buttons(row, col):
    button = buttons[row][col]
    button.config(text=player, state=tk.DISABLED)

# game won
def main_game_logic():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True

    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# game tie
def no_more_moves():
    return all(all(cell != '' for cell in row) for row in board)

# switch player
def switch():
    global player
    player = 'O' if player == 'X' else 'X'

# resetting the game
def reset():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state=tk.NORMAL)
            board[i][j] = ''
    global player
    player = 'X'

# 3*3 buttons
buttons = [[tk.Button(root, text='', font=('Helvetica, 16'), width=5, height=2, command=lambda row=i, col=j: on_click(row, col)) for j in range((3))] for i in range(3)]

# creating 3*3 grid
for i in range(3):
    # rows to expand proportionally
    root.rowconfigure(i, weight=1)
    for j in range(3):
        # columns to expand proportionally
        root.columnconfigure(j, weight=1)
        # adding sticky to the grid to make it fill the space in all 4 directions when expanded
        buttons[i][j].grid(row=i, column=j, sticky='nsew')

# puts everything on the display, and responds to user input until the program terminates
root.mainloop()
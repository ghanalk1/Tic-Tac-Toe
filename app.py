import random
import tkinter as tk
from tkinter import messagebox

# initializing player and board
player = 'X'
opponent = 'O'

current_player = player
board = [['' for j in range(3)] for i in range(3)]

# main window and master
root = tk.Tk()
root.geometry("500x400+720+200")
root.title('Tic Tac Toe')

# function to initiate on click
def player_moves(row, col):
    global current_player, board

    # updating the board and buttons
    # if board[row][col] == '':
    board[row][col] = player
    update_buttons(row ,col)

    # checking if the game is won or tied and then resetting the game
    if main_game_logic(player):
        messagebox.showinfo('Game Over', f'Congratulations! You won.')
        reset()
    elif no_more_moves():
        messagebox.showinfo('Game Over', 'No more moves possible, the game is tied.')
        reset()
    else:
        switch()
        # once the player == 'O', exceuted after a delay
        #root.after(1000, computer)
        if current_player == opponent:
            best_move = computer_minimax(False)
            row, col = best_move['position']
            board[row][col] = opponent
            update_buttons(row, col)

            if main_game_logic(opponent):
                messagebox.showinfo('Game Over', 'You lost, loser!')
                reset()
            elif no_more_moves():
                messagebox.showinfo('Game Over', 'No more moves possible, the game is tied.')
                reset()
            else:
                switch()

# updating buttons with 'X' or 'O'
def update_buttons(row, col):
    button = buttons[row][col]
    button.config(text=current_player, state=tk.DISABLED)

# game logic of winning
def main_game_logic(player_or_opponent):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player_or_opponent:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player_or_opponent:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player_or_opponent:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player_or_opponent:
        return True
    return False

# game tie
def no_more_moves():
    return all(all(cell != '' for cell in row) for row in board)

# switch player
def switch():
    global current_player
    current_player = player if current_player == opponent else opponent

# resetting the game
def reset():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state=tk.NORMAL)
            board[i][j] = ''
    global current_player
    current_player = player

# naive computer ai
def computer():
    # randomly selecting move
    possible_moves = [(i,j) for j in range(3) for i in range(3) if board[i][j] == '']
    row, col = random.choice(possible_moves)
    # time.sleep(3)
    board[row][col] = player
    update_buttons(row, col)

    # checking if the game is won or tied and then resetting the game
    if main_game_logic():
        messagebox.showinfo('Game Over', f'Congratulations Player {player}! You won.')
        reset()
    elif no_more_moves():
        messagebox.showinfo('Game Over', 'No more moves possible, the game is tied.')
        reset()
    else:
        switch()

# all possible moves for minimax
def all_possible_moves():
    possible_moves = [(i,j) for j in range(3) for i in range(3) if board[i][j] == '']
    return possible_moves

# base cases
def evaluate():
    if main_game_logic(player):
        return 1
    elif main_game_logic(opponent):
        return -1
    else:
        return 0

# counting blank cells on the board
def blank_cells(board):
    return sum(row.count('') for row in board)

# competitve computer ai using minimax algorithm
def computer_minimax(is_maximizing: bool):
    score = evaluate()

    # base conditions
    if score == 1 or score == -1:
        return {'score': score * (blank_cells(board) + 1), 'position': None}
    if no_more_moves():
        return {'score': 0, 'position': None}
    
    if is_maximizing: # i.e. 'X'
        best = {'score': float('-inf'), 'position': None}
        for i,j in all_possible_moves():
            board[i][j] = player
            temp = computer_minimax(False)

            board[i][j] = ''
            temp['position'] = (i,j)

            if temp['score'] > best['score']:
                best = temp
        return best
    else:
        best = {'score': float('inf'), 'position': None}
        for i,j in all_possible_moves():
            board[i][j] = opponent
            temp = computer_minimax(True)

            board[i][j] = ''
            temp['position'] = (i,j)

            if temp['score'] < best['score']:
                best = temp
        return best

# 3*3 buttons
buttons = [[tk.Button(root, text='', font=('Helvetica, 16'), width=5, height=2, command=lambda row=i, col=j: player_moves(row, col)) for j in range((3))] for i in range(3)]

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

import tkinter
from tkinter import messagebox
import random



board = [[' ' for _ in range(3)] for _ in range(3)]

lose_messages = ["another try", "NOPE", "maybe one day", "Saw it coming"," oops.", "BUH-BYEEE👋🏾"]
tie_messages = ["Mid Game", "Boring", "Try Harder", "Nice try", " maybe another", "you can't win."]


def display_random_message(messages):
    random_message = random.choice(messages)
    messagebox.showinfo("Game Over", random_message)


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
                all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def find_best_move(board):
    best_move = None
    best_score = -float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move


def minimax(board, depth, is_maximizing):
    scores = {'X': -1, 'O': 1, 'tie': 0}

    if check_win(board, 'O'):
        return scores['O']

    if check_win(board, 'X'):
        return scores['X']

    if is_board_full(board):
        return scores['tie']

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score

    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score


def player_move(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state='disabled')

        if check_win(board, 'X'):
            messagebox.showinfo("Game Over", "You win!")
            reset_game()
            return

        if is_board_full(board):
            display_random_message(tie_messages)
            reset_game()
            return

       
        ai_move()

def ai_move():
   best_move = find_best_move(board)
   if best_move:
        row, col = best_move
        board[row][col] = 'O'
        buttons[row][col].config(text='O', state='disabled')

        if check_win(board, 'O'):
            display_random_message(lose_messages)
            reset_game()
            return

        if is_board_full(board):
            display_random_message(tie_messages)
            reset_game()
            return


def reset_game():
    global board
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
            buttons[i][j].config(text=' ', state='active')


root = tkinter.Tk()
root.title("Tic-Tac-Toe")


buttons = [[None, None, None], [None, None, None], [None, None, None]]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tkinter.Button(root, text=' ', font=('normal', 20), height=2, width=5,
                                      command=lambda i=i, j=j: player_move(i, j))
        buttons[i][j].grid(row=i, column=j)


root.mainloop()














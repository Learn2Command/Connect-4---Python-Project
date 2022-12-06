# Importing global modules that will be used to run menu, pygame, AI functions.

from tkinter import *
import numpy as np
import random
import pygame
import sys
import math

pygame.init() # Initialize all imported pygame modules.
pygame.event.get() # Handles the internal events and retrieves a list of external events.

# Setting global variable colors for board and pieces.

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = WHITE


# Setting global variables for row and column count for the game board.

ROW_COUNT = 6
COLUMN_COUNT = 7


# Defining a function for playing with two local players. 
# This function will be called to the menu button twoplayer and run the Connect 4 code that allows players to alternate.

def two_player():
    def create_board():
        board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return board

    def drop_piece(board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(board, col):
        return board[ROW_COUNT - 1][col] == 0

    def get_next_open_row(board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def print_board(board):
        print(np.flip(board, 0))

    def winning_move(board, piece):
        # Check horizontal locations for win.
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # Check vertical locations for win.
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # Check positively sloped diaganols.
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diaganols.
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True

        # Drawing the board with rectangle and circles, as well as adding the colors and sizes.
    def draw_board(board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)
       
        # Game Loop.
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Mouse Button event is based on whose turn it is and drops the piece based off of that.
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                # print(event.pos)
                
                # Ask for Player 1 Input (Red).
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render("Player 1 Wins!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True


                # Ask for Player 2 Input (Yellow).
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render("Player 2 Wins!", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True

                print_board(board)
                draw_board(board)
                # The only way a turn can change is after a valid piece has been dropped. It will then start back at the top of the loop.
                # and wait until the player picks.
                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(1)
    from sys import exit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                

# Defining a function for playing against AI/Computer. This function will be called to the menu button playcomp and run the Connect 4 with AI code held within.

def play_comp():
    PLAYER = 0
    AI = 1

    EMPTY = 0
    PLAYER_PIECE = 1
    AI_PIECE = 2

    WINDOW_LENGTH = 4

    def create_board():
        board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return board

    def drop_piece(board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(board, col):
        return board[ROW_COUNT - 1][col] == 0

    def get_next_open_row(board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def print_board(board):
        print(np.flip(board, 0))

    def winning_move(board, piece):
        # Check Horizontal locations for win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # Check Vertical locations for win.
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # Check Positively sloped diaganols.
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True

        # Check Negatively sloped diaganols.
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True
    
    # The code below.
    def evaluate_window(window, piece):
        score = 0
        opp_piece = PLAYER_PIECE
        if piece == PLAYER_PIECE:
            opp_piece = AI_PIECE
 
        # This function corresponds with the score positions. 
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5 # We weight us getting a three in a row vs the AI (opp_piece).
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score
    
    def score_position(board, piece):
        score = 0
        
        # Scoring the center columns and adding preference for center pieces.
        # Creates more opportunities with the diagnols, horizontals, etc. if you have the center pieces. 
        # Using an array to store multiple values and i as a temporary variable to store the integer value.
        ## Score center column.
        center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        ## Score Horizontal.
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(COLUMN_COUNT - 3):
                window = row_array[c:c + WINDOW_LENGTH]
                score += evaluate_window(window, piece)

        ## Score Vertical.
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(ROW_COUNT - 3):
                window = col_array[r:r + WINDOW_LENGTH]
                score += evaluate_window(window, piece)

        ## Score Positive sloped diagonal.
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
                score += evaluate_window(window, piece)
       
        ## Score Negative sloped diaganols.
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
                score += evaluate_window(window, piece)

        return score
    # We are defining who wins the game: us, the opponent, or if all the pieces were used for a total of three conditions.
    def is_terminal_node(board):
        return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(
            get_valid_locations(board)) == 0

    def minimax(board, depth, alpha, beta, maximizingPlayer):
        valid_locations = get_valid_locations(board)
        is_terminal = is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if winning_move(board, AI_PIECE):
                    return (None, 100000000000000)
                elif winning_move(board, PLAYER_PIECE):
                    return (None, -10000000000000)
                else:  # Game is over, no more valid moves
                    return (None, 0)
            else:  # Depth is zero
                return (None, score_position(board, AI_PIECE)) 
        if maximizingPlayer: # AI player
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, AI_PIECE)
                new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player (Us).
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, PLAYER_PIECE)
                new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value: 
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value # Returns the score and column that produced that score.
  
    # Shows which columns we can drop a piece in and evaluate from there. We create an empty list since we don't have to figure out if it's valid or not.
    def get_valid_locations(board):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if is_valid_location(board, col):
                valid_locations.append(col)
        return valid_locations

    def pick_best_move(board, piece):
        # We created a new memory location (temp_board and board.copy()) so that it doesn't modify the original board while also keeping track of the score.
        valid_locations = get_valid_locations(board)
        best_score = -10000
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, piece)
            score = score_position(temp_board, piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col

      # Drawing the board with rectangle and circles, as well as adding the colors and sizes.
    def draw_board(board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == PLAYER_PIECE:
                    pygame.draw.circle(screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board[r][c] == AI_PIECE:
                    pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    board = create_board()
    print_board(board)
    game_over = False

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(PLAYER, AI)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == PLAYER:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_PIECE)

                        if winning_move(board, PLAYER_PIECE):
                            label = myfont.render("You Win!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True

                        turn += 1
                        turn = turn % 2

                        print_board(board)
                        draw_board(board)

        # Ask for Player 2 Input.
        if turn == AI and not game_over:

            # col = random.randint(0, COLUMN_COUNT-1)
            # col = pick_best_move(board, AI_PIECE)
            col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

            if is_valid_location(board, col):
                # pygame.time.wait(500)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = myfont.render("Computer Wins!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(1)
    
    from sys import exit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

# Setting root variable to call Tkinter
 
root = Tk()

# Adds a Menu to choose between local or AI / main menu with Tkinter.

menubar = Menu(root) 
filemenu = Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# Title of the game. Importing png file to use as logo on main menu


root.title('Connect 4') 
img = PhotoImage(file='connect4logo.png') # Importing the image we want to display as our logo.
Label(
    root,
    image=img
).pack()

# Icon Clip Art

ico = Image.open('Connect 4 clip art.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Adds a label to display group names.

lbl = Label(root, text="""
Created By Geoffrey Chambers, Estuardo Mendez, Tahlia Canovas, and Jimmy Riera
""", fg='blue', font=("Helvetica", 10), background='white')
lbl.place(x=40,y=195)
lbl.pack(expand=YES, fill=BOTH)

# Adds the option to choose between local, vs Comp play, or Quit on the menu using TKinter.

twoplayer = Button(root, text="Local Multiplayer", pady=5, padx=20, command=two_player)
playcomp = Button(root, text="Play Computer", pady=5, padx=20, command=play_comp)
quitbutton = Button(root, text="Quit", pady=5, padx=20, command=root.destroy)
twoplayer.pack()
playcomp.pack()
quitbutton.pack()

# Adds background music while playing the game by importing file

pygame.mixer.music.load('arcademusic.wav')
pygame.mixer.music.play(-1,0.0)
musicPlaying = True

#if event.type == KEYDOWN:
    #if event.key == K_m:
        #if musicPlaying:
            #pygame.mixer.music.stop()
        #else:
            #pygame.mixer.music.play(-1, 0.0)
        #musicPlaying = not musicPlaying

root.mainloop()

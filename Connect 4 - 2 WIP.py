# Importing global modules that will be used to run menu, pygame, AI functions.

from tkinter import *
import numpy as np
import random
import pygame
import sys
import math
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk

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
        """creates a board using row and column count provided for local play"""
        game_board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return game_board

    def drop_piece(game_board, row, col, piece):
        """returns grid status after a piece is dropped in local play"""
        game_board[row][col] = piece

    def is_valid_location(game_board, col):
        return game_board[ROW_COUNT - 1][col] == 0

    def get_next_open_row(game_board, col):
        for r in range(ROW_COUNT):
            if game_board[r][col] == 0:
                return r

    def print_board(game_board):
        """printing the board in a 6x7 form for local play"""
        print(np.flip(game_board, 0))

    def winning_move(game_board, piece):
        # Check horizontal locations for win.
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if game_board[r][c] == piece and game_board[r][c + 1] == piece and game_board[r][c + 2] == piece and game_board[r][
                    c + 3] == piece:
                    return True

        # Check vertical locations for win.
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if game_board[r][c] == piece and game_board[r + 1][c] == piece and game_board[r + 2][c] == piece and game_board[r + 3][
                    c] == piece:
                    return True

        # Check positively sloped diaganols.
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if game_board[r][c] == piece and game_board[r + 1][c + 1] == piece and game_board[r + 2][c + 2] == piece and \
                        game_board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diaganols.
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if game_board[r][c] == piece and game_board[r - 1][c + 1] == piece and game_board[r - 2][c + 2] == piece and \
                        game_board[r - 3][c + 3] == piece:
                    return True

        # Drawing the board with rectangle and circles, as well as adding the colors and sizes.
    def draw_board(game_board):
        """draws out board with provided colors and sizes on local play"""
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if game_board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif game_board[r][c] == 2:
                    pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    game_board = create_board()
    print_board(game_board)
    game_over = False
    turn = 0

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(game_board)
    pygame.display.update()

    myfont = pygame.font.SysFont("Veranda", 75)
       
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

                    if is_valid_location(game_board, col):
                        row = get_next_open_row(game_board, col)
                        drop_piece(game_board, row, col, 1)

                        if winning_move(game_board, 1):
                            label = myfont.render("Player 1 Wins!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True


                # Ask for Player 2 Input (Yellow).
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(game_board, col):
                        row = get_next_open_row(game_board, col)
                        drop_piece(game_board, row, col, 2)

                        if winning_move(game_board, 2):
                            label = myfont.render("Player 2 Wins!", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True

                print_board(game_board)
                draw_board(game_board)
                # The only way a turn can change is after a valid piece has been dropped. It will then start back at the top of the loop.
                # and wait until the player picks.
                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(1000)
    from sys import exit
    while True:
        # load button images
        start_img = pygame.image.load('replayb.png').convert_alpha()
        exit_img = pygame.image.load('exitb.png').convert_alpha()

        # create button instances
        start_button = RQButton(150, 350, start_img, 0.5)
        exit_button = RQButton(370, 350, exit_img, 0.5)

        # game loop
        run = True
        while run:

            if start_button.draw(screen):
                run = two_player()
            if exit_button.draw(screen):
                run = False

            # event handler
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
        pygame.quit()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
# Adding comment for separation between two player code and AI Code
# Adding comment for separation and to differentiate more readily between AI code and two player code
# Defining a function for playing against AI/Computer. This function will be called to the menu button playcomp and run the Connect 4 with AI code held within.

def play_comp():
    PLAYER = 0
    AI = 1

    EMPTY = 0
    PLAYER_PIECE = 1
    AI_PIECE = 2

    WINDOW_LENGTH = 4

    def create_board():
        """creates a board using row and column count provided for AI play"""
        game_board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return game_board

    def drop_piece(game_board, row, col, piece):
        """returns grid status after a piece is dropped in AI play"""
        game_board[row][col] = piece

    def is_valid_location(game_board, col):
        return game_board[ROW_COUNT - 1][col] == 0

    def get_next_open_row(game_board, col):
        for r in range(ROW_COUNT):
            if game_board[r][col] == 0:
                return r

    def print_board(game_board):
        """printing the board in a 6x7 form for AI play"""
        print(np.flip(game_board, 0))

    def winning_move(game_board, piece):
        # Check Horizontal locations for win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if game_board[r][c] == piece and game_board[r][c + 1] == piece and game_board[r][c + 2] == piece and game_board[r][
                    c + 3] == piece:
                    return True

        # Check Vertical locations for win.
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if game_board[r][c] == piece and game_board[r + 1][c] == piece and game_board[r + 2][c] == piece and game_board[r + 3][
                    c] == piece:
                    return True

        # Check Positively sloped diaganols.
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if game_board[r][c] == piece and game_board[r + 1][c + 1] == piece and game_board[r + 2][c + 2] == piece and \
                        game_board[r + 3][c + 3] == piece:
                    return True

        # Check Negatively sloped diaganols.
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if game_board[r][c] == piece and game_board[r - 1][c + 1] == piece and game_board[r - 2][c + 2] == piece and \
                        game_board[r - 3][c + 3] == piece:
                    return True
    
    # This function creates PLAYER_PIECE & AI_PIECE.
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
    
    def score_position(game_board, piece):
        score = 0
        
        # Scoring the center columns and adding preference for center pieces.
        # Creates more opportunities with the diagnols, horizontals, etc. if you have the center pieces. 
        # Using an array to store multiple values and i as a temporary variable to store the integer value.
        ## Score center column.
        center_array = [int(i) for i in list(game_board[:, COLUMN_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        ## Score Horizontal.
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(game_board[r, :])]
            for c in range(COLUMN_COUNT - 3):
                window = row_array[c:c + WINDOW_LENGTH]
                score += evaluate_window(window, piece)

        ## Score Vertical.
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(game_board[:, c])]
            for r in range(ROW_COUNT - 3):
                window = col_array[r:r + WINDOW_LENGTH]
                score += evaluate_window(window, piece)

        ## Score Positive sloped diagonal.
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [game_board[r + i][c + i] for i in range(WINDOW_LENGTH)]
                score += evaluate_window(window, piece)
       
        ## Score Negative sloped diaganols.
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [game_board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
                score += evaluate_window(window, piece)

        return score
    # We are defining who wins the game: us, the opponent, or if all the pieces were used for a total of three conditions.
    def is_terminal_node(game_board):
        return winning_move(game_board, PLAYER_PIECE) or winning_move(game_board, AI_PIECE) or len(
            get_valid_locations(game_board)) == 0

    def minimax(game_board, depth, alpha, beta, maximizingPlayer):
        valid_locations = get_valid_locations(game_board)
        is_terminal = is_terminal_node(game_board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if winning_move(game_board, AI_PIECE):
                    return (None, 100000000000000)
                elif winning_move(game_board, PLAYER_PIECE):
                    return (None, -10000000000000)
                else:  # Game is over, no more valid moves
                    return (None, 0)
            else:  # Depth is zero
                return (None, score_position(game_board, AI_PIECE)) 
        if maximizingPlayer: # AI player
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(game_board, col)
                board_copy = game_board.copy()
                drop_piece(board_copy, row, col, AI_PIECE)
                new_score = minimax(board_copy, depth - 1, alpha, beta, False)[1]
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
                row = get_next_open_row(game_board, col)
                board_copy = game_board.copy()
                drop_piece(board_copy, row, col, PLAYER_PIECE)
                new_score = minimax(board_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value: 
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value # Returns the score and column that produced that score.
  
    # Shows which columns we can drop a piece in and evaluate from there. We create an empty list since we don't have to figure out if it's valid or not.
    def get_valid_locations(game_board):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if is_valid_location(game_board, col):
                valid_locations.append(col)
        return valid_locations

    def pick_best_move(game_board, piece):
        # We created a new memory location (temp_board and board.copy()) so that it doesn't modify the original board while also keeping track of the score.
        valid_locations = get_valid_locations(game_board)
        best_score = -10000
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(game_board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, piece)
            score = score_position(temp_board, piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col

      # Drawing the board with rectangle and circles, as well as adding the colors and sizes.
    def draw_board(game_board):
        """draws out board with provided colors and sizes on AI play"""
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if game_board[r][c] == PLAYER_PIECE:
                    pygame.draw.circle(screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif game_board[r][c] == AI_PIECE:
                    pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    game_board = create_board()
    print_board(game_board)
    game_over = False

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(game_board)
    pygame.display.update()

    myfont = pygame.font.SysFont("Veranda", 75)

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

                    if is_valid_location(game_board, col):
                        row = get_next_open_row(game_board, col)
                        drop_piece(game_board, row, col, PLAYER_PIECE)

                        if winning_move(game_board, PLAYER_PIECE):
                            label = myfont.render("You Win!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True

                        turn += 1
                        turn = turn % 2

                        print_board(game_board)
                        draw_board(game_board)

        # Ask for Player 2 Input.
        if turn == AI and not game_over:

            # col = random.randint(0, COLUMN_COUNT-1)
            # col = pick_best_move(board, AI_PIECE)
            col, minimax_score = minimax(game_board, 5, -math.inf, math.inf, True)

            if is_valid_location(game_board, col):
                # pygame.time.wait(500)
                row = get_next_open_row(game_board, col)
                drop_piece(game_board, row, col, AI_PIECE)

                if winning_move(game_board, AI_PIECE):
                    label = myfont.render("Computer Wins!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                print_board(game_board)
                draw_board(game_board)

                turn += 1
                turn = turn % 2

        if game_over: #1 millisecond wait time to interact with UI after game over
            pygame.time.wait(1000)
    
    from sys import exit #Solves issue with quitting after game loop is complete
    while True:
        # load button images
        start_img = pygame.image.load('replayb.png').convert_alpha()
        exit_img = pygame.image.load('exitb.png').convert_alpha()

        # create button instances
        start_button = RQButton(150, 350, start_img, 0.5)
        exit_button = RQButton(370, 350, exit_img, 0.5)

        # game loop
        run = True
        while run:

            if start_button.draw(screen):
                run = play_comp()
            if exit_button.draw(screen):
                run = False

            # event handler
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
        pygame.quit()
        
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

# Icon Clip Art imported and displayed on menu bar

ico = Image.open('Connect 4 clip art.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Adds a label to display group names.

lbl = Label(root, text="""
Created By Geoffrey Chambers, Estuardo Mendez, Tahlia Canovas, and Jimmy Riera
""", fg='blue', font=("Helvetica", 10), background='white')
lbl.place(x=40,y=195)
lbl.pack(expand=YES, fill=BOTH)

class RQButton():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

# # Adding Player Names for Two Player Game
# 
# 
# def player_names():
# 
#     top = Toplevel()
#     top.title('Input Player Names')
#     top.geometry('400x200')
#     global play2p1
#     global play2p2
#     play2p1 = []
#     play2p2 = []
# 
#     #def list_names():
# 
# 
#     def getplayer1():
#         p1name = Label(top, text=name_p1.get() + ", Ready to Play!")
#         p1name.pack()
#         return p1name
# 
#     def getplayer2():
#         p2name = Label(top, text=name_p2.get() + ", Ready to Play!")
#         p2name.pack()
#         return p2name
# 
#     def two_player_button():
#         play2p = two_player()
#         return play2p
# 
#     def close_window():
#         top.destroy()
#         top.update()
# 
#     Label(top, text="Enter Player 1 Name").pack()
#     global name_p1
#     name_p1 = Entry(top)
#     name_p1.pack()
#     play2p1.append(getplayer1)
#     name_p1.insert(0, "Player 1")
# 
#     Button(top, text="Register Player 1", command=getplayer1).pack()
# 
#     Label(top, text="Enter Player 2 Name").pack()
#     global name_p2
#     name_p2 = Entry(top)
#     name_p2.pack()
#     play2p2.append(getplayer2)
#     name_p2.insert(0, "Player 2")
# 
#     Button(top, text="Register Player 2", command=getplayer2).pack()
# 
#     Button(top, text="Play Game", pady=5, padx=20, command=two_player)
#     playgame = Button(top, text="Play Game", pady=5, padx=20, command=lambda: [close_window(), two_player_button()])
#     playgame.pack()
# 
# 
# #Adding Player Name for One Player vs Computer Game
# 
# def player_names2():
# 
#     top = Toplevel()
#     top.title('Input Player Name')
#     top.geometry('400x100')
# 
#     def get_player1():
#         p1name = name_cp1.get()
#         return messagebox.showinfo('message', f'{p1name}, Ready to Play!')
# 
#     def one_player_button():
#         play1p = play_comp()
#         return play1p
# 
#     def close_window():
#         top.destroy()
#         top.update()
# 
#     Label(top, text="Enter Player Name").pack()
#     global name_cp1
#     name_cp1 = Entry(top)
#     name_cp1.pack()
# 
#     Button(top, text="Register Player", command=get_player1).pack()
#     Button(top, text="Play Game", pady=5, padx=20, command=play_comp)
#     playgame = Button(top, text="Play Game", pady=5, padx=20, command=lambda: [close_window(), one_player_button()])
#     playgame.pack()


#Importing Music File To Use as Background Music for the Game

pygame.mixer.music.load('arcademusic.wav')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
music_paused = False
muted = FALSE

# Function for volume level at max on
def set_vol(val):
    """set volume control for music which will allow following function to call"""
    volume = float(val) / 100
    mixer.music.set_volume(volume)
    
    # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1

    # Function to toggle volume to mute or sound on and off
def mute_music():
    """mute and unmute music"""
    global muted
    if muted:  # Unmute the music
        pygame.mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        scale.set(70)
        muted = FALSE
    else:  # mute the music
        pygame.mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE

# Adds Button and Icon to Toggle Sound On and Off as well as volume control sets
        
mutePhoto = PhotoImage(file='mute.png')
volumePhoto = PhotoImage(file='volume.png')
volumeBtn = Button(root, image=volumePhoto, command=mute_music)
scale = ttk.Scale()
scale.set(70)  # implement the default value of scale when music player starts
pygame.mixer.music.set_volume(0.7)

# Adds the option to choose between local, vs Comp play, or Quit on the menu using TKinter.

twoplayer = Button(root, text="Local Multiplayer", pady=5, padx=20, command=two_player)
playcomp = Button(root, text="Play Computer", pady=5, padx=20, command=play_comp)
quitbutton = Button(root, text="Quit", pady=5, padx=20, command=root.destroy)
twoplayer.pack() #Two Player Button
playcomp.pack() # Play Computer Button
quitbutton.pack() #Quit Button
volumeBtn.pack(side="right") #Sound on and off button placed in bottom right of main menu

#Anchors Tkinter main loop to root

root.mainloop()

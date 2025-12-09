import pygame as pg
import sys
import time
from pygame.locals import *

# ========= GLOBAL =========
XO = 'x'
winner = None
draw = None

width = 400
height = 400

# WARNA BARU (HITAM MERAH)
white = (255, 255, 255)
black = (0, 0, 0)
red = (220, 0, 0)
line_color = red

board = [[None] * 3 for _ in range(3)]

pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100))
pg.display.set_caption("Tic Tac Toe")

player1_name = ""
player2_name = ""

font_big = pg.font.Font(None, 50)
font_small = pg.font.Font(None, 35)


# ========= TEXT INPUT =========
def text_input(prompt):
    input_text = ""
    typing = True

    while typing:
        screen.fill(black)

        label = font_small.render(prompt, True, red)
        screen.blit(label, (50, 120))

        input_box = pg.Rect(50, 170, 300, 50)
        pg.draw.rect(screen, red, input_box, 2)

        text_surface = font_small.render(input_text, True, red)
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

        pg.display.update()

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return input_text if input_text.strip() != "" else "Player"
                elif event.key == K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode


# ========= MAIN MENU =========
def main_menu():
    global player1_name, player2_name

    menu_running = True

    while menu_running:
        screen.fill(black)

        title = font_big.render("TIC TAC TOE", True, red)
        screen.blit(title, (110, 40))

        btn1 = pg.Rect(100, 130, 200, 50)
        btn2 = pg.Rect(100, 210, 200, 50)
        btn_start = pg.Rect(100, 300, 200, 50)

        # BUTTONS
        pg.draw.rect(screen, (50, 0, 0), btn1)
        pg.draw.rect(screen, (50, 0, 0), btn2)
        pg.draw.rect(screen, red, btn_start)

        # TEXT
        screen.blit(font_small.render("Nama Player 1", True, white), (120, 140))
        screen.blit(font_small.render("Nama Player 2", True, white), (120, 220))
        screen.blit(font_small.render("MULAI GAME", True, white), (140, 310))

        # NAMA DITAMPILKAN SECARA RAPI
        name1 = font_small.render(f"{player1_name}", True, red)
        name2 = font_small.render(f"{player2_name}", True, red)
        screen.blit(name1, (110, 175))
        screen.blit(name2, (110, 255))

        pg.display.update()

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if btn1.collidepoint(event.pos):
                    player1_name = text_input("Nama Player 1:")
                if btn2.collidepoint(event.pos):
                    player2_name = text_input("Nama Player 2:")
                if btn_start.collidepoint(event.pos):
                    if player1_name == "": player1_name = "Player 1"
                    if player2_name == "": player2_name = "Player 2"
                    menu_running = False


# ========= GAME SCREEN =========
def game_initiating_window():
    screen.fill(black)

    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_color, (2*width/3, 0), (2*width/3, height), 7)

    pg.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, line_color, (0, 2*height/3), (width, 2*height/3), 7)

    draw_status()


def draw_status():
    global draw

    screen.fill(red, (0, 400, 500, 100))

    if winner is None:
        player_turn = player1_name if XO == 'x' else player2_name
        message = f"{player_turn}'s Turn"
    else:
        win_name = player1_name if winner == 'x' else player2_name
        message = f"{win_name} Won!"

    if draw:
        message = "Game Draw!"

    text = font_small.render(message, True, white)
    text_rect = text.get_rect(center=(width / 2, 430))
    screen.blit(text, text_rect)

    # RESET BUTTON (TENGAH)
    reset_btn = pg.Rect(width // 2 - 60, 450, 120, 35)
    pg.draw.rect(screen, black, reset_btn)

    reset_text = font_small.render("RESET", True, red)
    reset_rect = reset_text.get_rect(center=reset_btn.center)
    screen.blit(reset_text, reset_rect)

    pg.display.update()


# ========= CHECK WIN =========
def check_win():
    global winner, draw

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != None:
            winner = board[row][0]
            y = row * height/3 + height/6
            pg.draw.line(screen, red, (20, y), (380, y), 4)
            break

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != None:
            winner = board[0][col]
            x = col * width/3 + width/6
            pg.draw.line(screen, red, (x, 20), (x, 380), 4)
            break

    if board[0][0] == board[1][1] == board[2][2] != None:
        winner = board[0][0]
        pg.draw.line(screen, red, (20, 20), (380, 380), 4)

    if board[0][2] == board[1][1] == board[2][0] != None:
        winner = board[0][2]
        pg.draw.line(screen, red, (380, 20), (20, 380), 4)

    if all(all(row) for row in board) and winner is None:
        draw = True

    draw_status()


# ========= DRAW X O =========
def drawXO(row, col):
    global XO

    posx = (col - 1) * (width/3) + width/6
    posy = (row - 1) * (height/3) + height/6

    board[row - 1][col - 1] = XO

    if XO == "x":
        offset = 40
        pg.draw.line(screen, red, (posx - offset, posy - offset), (posx + offset, posy + offset), 6)
        pg.draw.line(screen, red, (posx + offset, posy - offset), (posx - offset, posy + offset), 6)
        XO = "o"
    else:
        pg.draw.circle(screen, red, (int(posx), int(posy)), 45, 6)
        XO = "x"

    pg.display.update()


# ========= USER CLICK =========
def user_click():
    x, y = pg.mouse.get_pos()

    # RESET BUTTON CLICK (TENGAH)
    if width//2 - 60 <= x <= width//2 + 60 and 450 <= y <= 485:
        reset_game()
        return

    if y > height:
        return

    col = 1 if x < width/3 else 2 if x < 2*width/3 else 3
    row = 1 if y < height/3 else 2 if y < 2*height/3 else 3

    if board[row - 1][col - 1] is None:
        drawXO(row, col)
        check_win()


def reset_game():
    global XO, winner, draw, board
    XO = 'x'
    winner = None
    draw = None
    board = [[None] * 3 for _ in range(3)]
    game_initiating_window()


# ========= START =========
main_menu()
game_initiating_window()

# ========= MAIN LOOP =========
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            user_click()

    pg.display.update()
    CLOCK.tick(fps)

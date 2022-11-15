import random

import pygame
import sys

from Square import Square

# Инициализация
pygame.init()


# Инициализация игрового поля
def init_game_field():
    choice = int(0)
    for xi in range(5):
        x = 5 + (130 * xi)
        for yi in range(5):
            y = 5 + (130 * yi)
            if xi == 1 or xi == 3:
                if yi in (0, 2, 4):
                    init_square(xi, yi, game_field, GREY, x, y, 0)
                else:
                    init_square(xi, yi, game_field, WHITE, x, y, 1)
            else:
                # init_square(xi, yi, game_field, COLORS[randint(0, 2)], x, y, 1)
                init_square(xi, yi, game_field, COLORS[list_for_random[choice]], x, y, 1)
                choice += 1


# Обновление игрового поля
def update_game_field():
    for xi in range(5):
        x = 5 + (130 * xi)
        for yi in range(5):
            y = 5 + (130 * yi)
            update_square(game_field, list_squares[yi][xi].color, list_squares[yi][xi].position)


def update_square(field, color, pos):
    size = (125, 125)
    pygame.draw.rect(field, color, (*pos, *size),border_radius=10)


# Инициализация кубиков
def init_square(xi, yi, field, color, x, y, can_remove):
    size = (125, 125)
    list_squares[yi][xi] = Square(xi, yi, color, (x, y), can_remove)
    pygame.draw.rect(field, list_squares[yi][xi].color, (*list_squares[yi][xi].position, *size),border_radius=10)


# Выход из игры
def exit_game():
    pygame.quit()
    sys.exit()


# Поиск кубика
def detected_square(x, y):
    for oc in range(5):
        for co in range(5):
            (init_x, init_y), final_x, final_y, flag = list_squares[co][oc].call_position()
            if x >= init_x and x <= final_x and y >= init_y and y <= final_y:
                return co, oc, list_squares[co][oc].call_can_remove(), list_squares[co][oc].color_square()


# Определение местоположения курсора в окне игры
def search(x, y):
    global score
    # Кнопка рестарт
    if x >= location_restart_button[0] + 2 and x <= location_restart_button[0] + 196 and y >= location_restart_button[
        1] + 2 and y <= location_restart_button[1] + 116:
        score = 0
        refresh_menu()
        button_restart()
    # Кнопка quit
    if x >= location_quit_button[0] + 2 and x <= location_quit_button[0] + 196 and y >= location_quit_button[
        1] + 20 and y <= location_quit_button[1] + 96:
        exit_game()
    # Игровое поле
    if x >= 280 and x <= 935 and y >= 180 and y <= 835:
        return detected_square(x - 280, y - 180)


# Обновление игровой области
def redrawGameWindow():
    game_field_fon.blit(game_field, (40, 160))
    sc.blit(game_field_fon, (240, 20))
    # Обновление
    pygame.display.update()


# Создание начальной последовательности кубиков на игровом поле
def create_new_random_location():
    global list_for_random
    list_for_random = [j for i in range(5) for j in range(3)]
    return random.shuffle(list_for_random)


# Функция кнопки Restart
def button_restart():
    init_game_field()
    redrawGameWindow()


def series_check():
    exercise_color = 0
    for j in range(0, 5, 2):
        for i in range(5):
            first = list_squares[i][j].color
            next_s = COLORS[exercise_color]
            if first == next_s:
                pass
            else:
                return 0
        exercise_color += 1
    return 1


# Задание цвета кубиков
def init_exercise():
    xix = 45
    yiy = 20
    for i in range(len(COLORS)):
        pygame.draw.rect(game_field_fon, COLORS[i], (xix, yiy, 125, 125),border_radius=10)
        xix += 260

#Обновление экрана (меню)
def refresh_menu():
    score_count = text2.render(f'{score}', 1, WHITE)
    sc.blit(screen_fon, (0, 0))
    sc.blit(score_table, (20, 20))
    sc.blit(blue_button, location_restart_button)
    sc.blit(red_button, location_quit_button)
    sc.blit(score_count, (110, 54))


location_restart_button = (20, 180)
location_quit_button = (20, 770)

# Основные цвета
RED = (100, 0, 0)
GREEN = (0, 100, 0)
BLUE = (0, 0, 100)
WHITE = (255, 255, 255)
GREY = (30, 30, 30)
BLACK = (0, 0, 0)
COLORS = [RED, GREEN, BLUE]

score = 0

# Окно игры
W, H = 1000, 900
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Аналог миниигры')

# Обновление экрана
FPS = 30
clock = pygame.time.Clock()

# Создание списка объектов (с ориентацией по вертикали)
list_squares = [[str(i) + str(g) for i in range(1, 6)] for g in range(1, 6)]
create_new_random_location()

screen_fon = pygame.image.load("image/fon_sovr.png").convert_alpha()
red_button = pygame.image.load("image/red_button.png").convert_alpha()
blue_button = pygame.image.load("image/blue_button.png").convert_alpha()
score_table = pygame.image.load("image/desk.png").convert_alpha()
game_field_fon = pygame.image.load("image/carbon.png").convert_alpha()
game_field_fon= pygame.transform.scale(game_field_fon,(735,850))
score_table = pygame.transform.scale(score_table, (200, 120))
red_button = pygame.transform.scale(red_button, (200, 120))
blue_button = pygame.transform.scale(blue_button, (200, 120))
screen_fon = pygame.transform.scale(screen_fon, (W, H))

# Меню игры
text = pygame.font.SysFont('arial', 36)
text2 = pygame.font.SysFont('monospace', 32)

restart_text = text.render('Restart', 1, WHITE)
qt_text = text.render('Quit', 1, WHITE)
score_text = text2.render('SCORE:', 1, WHITE)
score_count = text2.render(str(score), 1, WHITE)

sc.blit(screen_fon, (0, 0))
score_table.blit(score_text, (46, 6))
sc.blit(score_count, (90, 40))
sc.blit(score_table, (20, 20))
blue_button.blit(restart_text, (56, 36))
red_button.blit(qt_text, (74, 40))
sc.blit(blue_button, location_restart_button)
sc.blit(red_button, location_quit_button)

# Игровая область
pole = pygame.Surface((735, 850))
pole.fill(GREY)
game_field = pygame.Surface((655, 655))
game_field.fill(BLACK)

init_game_field()
init_exercise()
redrawGameWindow()

in_flag = 0
ex_flag = 0

while 1:
    clock.tick(FPS)
    global in_co, in_oc, in_color, ex_co, ex_oc, ex_numb_x, ex_numb_y, ex_color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()  # или pygame.quit() и flag = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                answer_search = search(*event.pos)
                if answer_search != None:
                    in_co, in_oc, in_flag, in_color = answer_search

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                answer_search = search(*event.pos)
                if answer_search != None:
                    if in_flag != 0:
                        ex_co, ex_oc, ex_flag, ex_color = answer_search
                    else:
                        in_flag = 0
                        ex_flag = 0

        elif ex_flag and in_flag:
            if (in_color == WHITE or ex_color == WHITE) and (in_co in (ex_co, ex_co - 1, ex_co + 1)) and (
                    in_oc in (ex_oc, ex_oc - 1, ex_oc + 1)) and (
                    (in_co + in_oc == ex_co + ex_oc + 1) or (in_co + in_oc == ex_co + ex_oc - 1)):
                list_squares[in_co][in_oc].overwriting(ex_color)
                list_squares[ex_co][ex_oc].overwriting(in_color)
                score += 1
                print(score)

            game_field.fill(BLACK)
            update_game_field()
            refresh_menu()

            in_flag = 0
            ex_flag = 0
            redrawGameWindow()


        elif series_check():
            exit_game()

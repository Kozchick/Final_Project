import pygame as pg
from pygame.locals import *
from sys import exit
import random

pg.init()
k = 1
Game_size = int(800 * k)
FPS = 60
Score = None
Name = 'name'
DISPLAY = pg.display.set_mode((Game_size, Game_size), RESIZABLE)
pg.display.set_caption('Flappy Bird')
Go_back_button_img = pg.image.load('Pictures/Buttons/Go_back.png')
Play_button_img = pg.image.load('Pictures/Buttons/Play.png')
Left_button_img = pg.image.load('Pictures/Buttons/Left.png')
Right_button_img = pg.image.load('Pictures/Buttons/Right.png')
Coming_soon = pg.image.load('Pictures/Buttons/Coming_soon.png')
Flappy_bird_start_img = pg.image.load('Pictures/Buttons/Flappy_bird_start.png')
Play_flappy_img = pg.image.load('Pictures/Buttons/Play_flappy.png')
Highscores = pg.image.load('Pictures/Buttons/Highscores.png')
FlappyBackground_img = pg.image.load('Pictures/Others/Background_new.png')
Bird_img = pg.image.load('Pictures/Others/Bird.png')
Column_img = pg.image.load('Pictures/Others/Collumn.png')
Game_over_img = pg.image.load('Pictures/Others/Game_over.png')
One_img = pg.image.load('Pictures/Digits/Numbers/One.png')
Two_img = pg.image.load('Pictures/Digits/Numbers/Two.png')
Three_img = pg.image.load('Pictures/Digits/Numbers/Three.png')
Four_img = pg.image.load('Pictures/Digits/Numbers/Four.png')
Five_img = pg.image.load('Pictures/Digits/Numbers/Five.png')
Six_img = pg.image.load('Pictures/Digits/Numbers/Six.png')
Seven_img = pg.image.load('Pictures/Digits/Numbers/Seven.png')
Eight_img = pg.image.load('Pictures/Digits/Numbers/Eight.png')
Nine_img = pg.image.load('Pictures/Digits/Numbers/Nine.png')
Zero_img = pg.image.load('Pictures/Digits/Numbers/Zero.png')
a = pg.image.load('Pictures/Digits/Letters/A.png')
B = pg.image.load('Pictures/Digits/Letters/B.png')
c = pg.image.load('Pictures/Digits/Letters/C.png')
d = pg.image.load('Pictures/Digits/Letters/D.png')
e = pg.image.load('Pictures/Digits/Letters/E.png')
f = pg.image.load('Pictures/Digits/Letters/F.png')
g = pg.image.load('Pictures/Digits/Letters/G.png')
h = pg.image.load('Pictures/Digits/Letters/H.png')
I0 = pg.image.load('Pictures/Digits/Letters/I.png')
j = pg.image.load('Pictures/Digits/Letters/J.png')
k = pg.image.load('Pictures/Digits/Letters/K.png')
L = pg.image.load('Pictures/Digits/Letters/L.png')
m = pg.image.load('Pictures/Digits/Letters/M.png')
n = pg.image.load('Pictures/Digits/Letters/N.png')
o = pg.image.load('Pictures/Digits/Letters/O.png')
p = pg.image.load('Pictures/Digits/Letters/P.png')
q = pg.image.load('Pictures/Digits/Letters/Q.png')
r = pg.image.load('Pictures/Digits/Letters/R.png')
s = pg.image.load('Pictures/Digits/Letters/S.png')
t = pg.image.load('Pictures/Digits/Letters/T.png')
u = pg.image.load('Pictures/Digits/Letters/U.png')
v = pg.image.load('Pictures/Digits/Letters/V.png')
w = pg.image.load('Pictures/Digits/Letters/W.png')
X = pg.image.load('Pictures/Digits/Letters/X.png')
Y = pg.image.load('Pictures/Digits/Letters/Y.png')
z = pg.image.load('Pictures/Digits/Letters/Z.png')
space = pg.image.load('Pictures/Digits/Symbols/Space.png')
two_points = pg.image.load('Pictures/Digits/Symbols/Two_points.png')
question = pg.image.load('Pictures/Digits/Symbols/Question.png')
point = pg.image.load('Pictures/Digits/Symbols/Point.png')
dictionary = {'0': Zero_img, '1': One_img, '2': Two_img, '3': Three_img, '4': Four_img, '5': Five_img, '6': Six_img,
              '7': Seven_img, '8': Eight_img, '9': Nine_img, 'a': a, 'b': B, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g,
              'h': h, 'i': I0, 'j': j, 'k': k, 'l': L, 'm': m, 'n': n, 'o': o, 'p': p, 'q': q, 'r': r, 's': s, 't': t,
              'u': u, 'v': v, 'w': w, 'x': X, 'y': Y, 'z': z, 'A': a, 'B': B, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g,
              'H': h, 'I': I0, 'J': j, 'K': k, 'L': L, 'M': m, 'N': n, 'O': o, 'P': p, 'Q': q, 'R': r, 'S': s, 'T': t,
              'U': u, 'V': v, 'W': w, 'X': X, 'Y': Y, 'Z': z, ' ': space, ':': two_points, '?': question, '.': point}
games = (('Flappy_bird_menu', Flappy_bird_start_img), ('Main_menu', Coming_soon))
games_buttons_size = 200
symbols_size = (13, 19)
clock = pg.time.Clock()
condition = 'Main_menu'
Black = (0, 0, 0)
White = (255, 255, 255)
Flappy_Background_size_x = FlappyBackground_img.get_width()
Flappy_Background_size_y = FlappyBackground_img.get_height()


class Picture:
    """Получает на вход координаты, размеры картинки и ее саму, а также дисплей для отображения. """
    def __init__(self, x, y, size_x, size_y, img, dis):
        self.size_y = int(size_y * k)
        self.size_x = int(size_x * k)
        self.dis = dis
        self.x = int(x * k)
        self.y = int(y * k)
        self.img = img

    def draw(self):
        """"Отображает картинку по параметрам. """
        self.dis.blit(pg.transform.scale(self.img, (self.size_x, self.size_y)), (self.x, self.y))


class Button:
    """Тот же Picture, но имеет еще один метод. """
    def __init__(self, x, y, size_x, size_y, img, dis):
        self.size_y = int(size_y * k)
        self.size_x = int(size_x * k)
        self.dis = dis
        self.x = int(x * k)
        self.y = int(y * k)
        self.img = img

    def draw(self):
        self.dis.blit(pg.transform.scale(self.img, (self.size_x, self.size_y)), (self.x, self.y))

    def press(self, event):
        """Получает на вход событие pygame, возвращает True если кнопка нажата, False если нет. """
        if event.type == pg.MOUSEBUTTONDOWN and 0 < event.pos[0] - self.x < self.size_x and 0 < event.pos[1] - self.y <\
                self.size_y:
            return True
        return False


class Background(pg.sprite.Sprite):
    """Класс Background создан для отображения фона. """
    def __init__(self, x, y, size_x, size_y, img, dis, left_neighbor, right_neighbor, group, delta):
        """Получает на вход: начальные координаты, размеры, картинку - фон, дисплей для отображения, наличие кусочков
        фона (соседей) слева, справа, свою группу, смещение при создании соседа (обычно равно размеру по х). """
        pg.sprite.Sprite.__init__(self)
        self.gen = (size_x, size_y, img, y)
        self.size_y = int(size_y * k)
        self.size_x = int(size_x * k)
        self.dis = dis
        self.x = int(x * k)
        self.y = int(y * k)
        self.img = pg.transform.scale(img, (self.size_x, self.size_y))
        self.delta = delta
        self.add(group)
        self.right_neighbor = right_neighbor
        self.left_neighbor = left_neighbor

    def update(self, speed, group):
        """Получает на вход смещение по х и группу для нового соседа. Отображет себя, создает себе соседей по
        необходимости, удаляет сея из всех групп по необходмости. """
        self.dis.blit(self.img, (int(self.x), int(self.y)))
        self.x += speed * k
        if self.left_neighbor and self.x < 0:
            self.left_neighbor = False
        if not self.left_neighbor and self.x + speed > 0:
            self.left_neighbor = True
            group.add(
                Background(self.x / k - self.delta, self.gen[3], self.gen[0], self.gen[1], self.gen[2], self.dis, False,
                           True, group, self.delta))
        if self.right_neighbor and self.x > Game_size - self.size_x:
            self.right_neighbor = False
        if not self.right_neighbor and self.x + speed < Game_size - self.size_x:
            self.right_neighbor = True
            group.add(
                Background(self.x / k + self.delta, self.gen[3], self.gen[0], self.gen[1], self.gen[2], self.dis, True,
                           False, group, self.delta))
        if self.x < -self.size_x or self.x > Game_size:
            self.kill()


class Column:
    """Создан для удобной работы с колонами в Flappy Bird, не является спрайтом, т. к. при объединении в группы
    update теряет возможность возвращать что либо. """
    def __init__(self, x, y):
        """На вход получает начальные координаты. """
        self.x = x * k
        self.y = y * k
        self.img = Column_img
        self.size_x = int(self.img.get_width() * k)
        self.size_y = int(self.img.get_height() * k)
        self.neighbor = False
        self.scored = False

    def update(self, col_speed, b_x, b_y, b_s_x, b_s_y, group):
        """На вход получвает величину смещения колоны, координаты птицы, ее размеры (т. к. птица вращается,
        это не константы), список колон. Смещает колону, проверяет столкновение птицы с собой (все константы связаны
        с картинкой колонны), создает другую колону и удаляет себя по необходимости, возвращает столкновение с птицей
        (True / False), и кол-во очков на которое нужно увеличить счет. """
        self.x += col_speed
        if not self.neighbor and self.x < 520 * k:
            self.neighbor = True
            y = self.y / k + random.randint(int(-100 * k), int(100 * k))
            if y > -88:
                y = -88
            elif y < -436:
                y = -436
            group.append(Column(870, y))
        DISPLAY.blit(pg.transform.scale(Column_img, (self.size_x, self.size_y)), (self.x, self.y))
        if not self.scored and self.size_x < b_x - self.x:
            self.scored = True
            return False, 1
        if -b_s_x < b_x - self.x < self.size_x and (b_y < self.y + 536 * k or b_y + b_s_y > self.y + 744 * k):
            return True, 0
        if self.x < -self.size_x:
            group.pop(0)
        return False, 0


def MainMenu():
    """Функция главного меню, создана дляы выбор игр (пока что не из чего выбирать). Отображает спсок игр,
    кнопки для выбора игры, голубой квадрат, показывающий, какая игра выбрана. Возвращает новое состояние и очки
    счета. Все числа указаны с учетом того, что дисплей 800х800 (вообще везде), изменения дисплея возможны благодаря
    коэффициенту k. """
    num_of_game = 0
    len_of_games = len(games)
    while True:
        DISPLAY.fill(Black)
        display_changing()
        buttons = (Button(300, 550, 200, 50, Play_button_img, DISPLAY),
                   Button(250, 375, 50, 50, Left_button_img, DISPLAY),
                   Button(500, 375, 50, 50, Right_button_img, DISPLAY))  # play, left, right
        for b in buttons:
            b.draw()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if num_of_game != 0 and buttons[1].press(event):
                num_of_game += 1
            if num_of_game != -len_of_games + 1 and buttons[2].press(event):
                num_of_game -= 1
            for i in range(0, len(games)):
                if buttons[0].press(event) and num_of_game == i:
                    return games[i][0], None
        mainmenu_pictures(num_of_game)
        pg.draw.rect(DISPLAY, (0, 128, 255), (int(295 * k), int(295 * k), int(210 * k), int(210 * k)), 5)
        pg.draw.rect(DISPLAY, Black, (0, Game_size, Game_size, Game_size))
        pg.draw.rect(DISPLAY, Black, (Game_size, 0, Game_size, Game_size))
        pg.display.update()
        clock.tick(FPS)


def FlappyBirdMenu(score, name):
    """Меню игры Flappy bird из него можно перейти в Рекорды, Главное меню и саму игру, здесь можно сменить имя. На
    вход получает очки счета и имя игрока. Оно отображает кнопки для совершения ранее указаных действий, а также Game
    over, если игрок проиграл. Для того чтобы изменить имя не нужно никуда нажимать, просто пололзуйтесь клавиатурой.
    Возвращает новое состояние и имя. """
    backgrounds = pg.sprite.Group()
    backgrounds.add(Background(-int(random.random()) * 32 + Flappy_Background_size_x, 0, Flappy_Background_size_x,
                               Flappy_Background_size_y, FlappyBackground_img, DISPLAY, False, False, backgrounds,
                               Flappy_Background_size_x))
    buttons = (Button(300, 550, 200, 50, Play_flappy_img, DISPLAY), Button(300, 490, 200, 50, Highscores, DISPLAY),
               Button(0, 0, 50, 50, Go_back_button_img, DISPLAY),
               Button(50, 0, symbols_size[0] * len('nickname: '), symbols_size[1], space, DISPLAY))
    if score:
        highscores_file = open('Highscores.txt', 'a')
        highscores_file.write(str(score) + ' ' + Name + '\n')
        highscores_file.close()
    while True:
        display_changing()
        backgrounds.update(0, backgrounds)
        if score is not None:
            Text_print('Game', (400, 50), 4, True)
            Text_print('over', (400, 50 + symbols_size[1] * 4), 4, True)
            Text_print('Your score: ' + str(score), (400, 50 + symbols_size[1] * 8), 2, True)
        Text_print('Nickname: ' + name, (50, 0), 2, False)
        for b in buttons:
            b.draw()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) != 12 and event.unicode != ' ':
                    name += event.unicode
            if buttons[0].press(event):
                return 'Flappy_bird_game', name
            if buttons[1].press(event):
                return 'Highscores_menu', name
            if buttons[2].press(event):
                return 'Main_menu', name
        pg.draw.rect(DISPLAY, Black, (0, Game_size, Game_size, Game_size))
        pg.draw.rect(DISPLAY, Black, (Game_size, 0, Game_size, Game_size))
        pg.display.update()
        clock.tick(FPS)


def FlappyBirdGame():
    """Функция игры Flappy bird. Создаются и движутся колоны, кусочки заднего фона, прыгает птица. Возвращает новое
    состояние и очки счета. """
    score = 0
    b_speedy = 0
    b_x = 200 * k
    b_y = 250 * k
    backgrounds_town = pg.sprite.Group()
    col_list = [Column(650, random.randint(-436, -88))]
    backgrounds_town.add(Background(-int(random.random()) * 32 + Flappy_Background_size_x, 0, Flappy_Background_size_x,
                                    Flappy_Background_size_y, FlappyBackground_img, DISPLAY, False, False,
                                    backgrounds_town, Flappy_Background_size_x))
    while True:
        b_a = 30 / FPS
        backgrounds_speed = -180 * k / FPS
        display_changing()
        b_speedy += b_a
        backgrounds_town.update(-30 / FPS, backgrounds_town)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN:
                b_speedy = -10
        b_y, b_angle, game_over, b_s_x, b_s_y = bird_update(b_x, b_y, b_speedy, 3)
        for i in col_list:
            concerns, score_plus = i.update(backgrounds_speed, b_x - b_s_x / 2, b_y - b_s_y / 2, b_s_x, b_s_y, col_list)
            if concerns:
                game_over = True
            score += score_plus
        Text_print(str(score), (Game_size / 2, 0), 2, True)
        if game_over:
            return 'Flappy_bird_menu', score
        pg.draw.rect(DISPLAY, Black, (0, Game_size, Game_size, Game_size))
        pg.draw.rect(DISPLAY, Black, (Game_size, 0, Game_size, Game_size))
        pg.display.update()
        clock.tick(FPS)


def HighscoreMenu():
    """Меню, где отображаются 10 лучших Рекордов в Flappy bird. Возвращает новое состояние. """
    buttons = (Button(0, 0, 50, 50, Go_back_button_img, DISPLAY),)
    Highsc0res('Highscores.txt')
    high = open('Highscores.txt', 'r')
    DISPLAY.fill(White)
    while True:
        display_changing()
        for b in buttons:
            b.draw()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if buttons[0].press(event):
                high.close()
                return 'Flappy_bird_menu', None
        i = 0
        for i0 in high:
            Text_print(str(i + 1) + '. ' + i0[:-1], (150 - symbols_size[0] * 2 * (len(str(i + 1)) - 1),
                                                     150 + i * symbols_size[1] * 2), 2, False)
            i += 1
        pg.draw.rect(DISPLAY, Black, (0, Game_size, Game_size, Game_size))
        pg.draw.rect(DISPLAY, Black, (Game_size, 0, Game_size, Game_size))
        pg.display.update()
        clock.tick(FPS)


def mainmenu_pictures(pos):
    """Функция, отображающая все каринки с играми главного меню, на вход получает номер текущей выбранной игры. """
    delta_pos = 250 * k
    xy = (Game_size - games_buttons_size * k) / 2
    for i in range(0, len(games)):
        DISPLAY.blit(pg.transform.scale(games[i][1], (int(games_buttons_size * k), int(games_buttons_size * k))),
                     ((xy + delta_pos * (i + pos)), xy))


def bird_update(x, y, speed, k1):
    """Функция обновленя состояния птицы. На вход получает ее координаты, ускорение (свободного падения), коэфициэнт
    поворота. Повернув под нужным углом отображает птицу, высчитывает ее новые парамеры и возвращает их. """
    game_over = False
    angle = -k1 * speed
    y += speed * k
    b_height = int(Bird_img.get_height() * k)
    b_width = int(Bird_img.get_width() * k)
    bird_img_rotate = pg.transform.rotate(pg.transform.scale(Bird_img, (b_width, b_height)), angle)
    rect = bird_img_rotate.get_rect(center=(x, y))
    DISPLAY.blit(bird_img_rotate, rect)
    if y > 688 * k - b_height / 2 or y < b_height / 2:
        game_over = True
    return y, angle, game_over, b_width, b_height


def display_changing():
    """Отвечает за изменние дисплея, а также параметров k и Game_size"""
    global k, Game_size
    Game_size = min(DISPLAY.get_width(), DISPLAY.get_height())
    k = Game_size / 800


def Text_print(txt, pos, x, center):
    """Отрисовывает текст txt в позици pos и коэффициентом увеличения размера х. center отвечаетт за то,
    будет ли первый элемент pos центром надписи или ее краем. """
    length = len(txt)
    if center:
        for i in range(0, length):
            try:
                DISPLAY.blit(pg.transform.scale(dictionary[txt[i]],
                                                (int(symbols_size[0] * x * k), int(symbols_size[1] * x * k))),
                             ((pos[0] + x * symbols_size[0] * (i - 0.5 * length)) * k, pos[1] * k))
            except KeyError:
                DISPLAY.blit(pg.transform.scale(question, (int(symbols_size[0] * x * k), int(symbols_size[1] * x * k))),
                             ((pos[0] + x * symbols_size[0] * (i - 0.5 * length)) * k, pos[1] * k))
    else:
        for i in range(0, length):
            try:
                DISPLAY.blit(pg.transform.scale(dictionary[txt[i]],
                                                (int(symbols_size[0] * x * k), int(symbols_size[1] * x * k))),
                             ((pos[0] + x * symbols_size[0] * i) * k, pos[1] * k))
            except KeyError:
                DISPLAY.blit(pg.transform.scale(question, (int(symbols_size[0] * x * k), int(symbols_size[1] * x * k))),
                             ((pos[0] + x * symbols_size[0] * i) * k, pos[1] * k))


def Highsc0res(name_of_file):
    """Работает с файлом, сортируя его по убываню очков. """
    highscores_file = open(name_of_file, 'r')
    list_of_highscores = []
    new_list_of_highscores = []
    list_of_scores = []
    for i in highscores_file:
        i = i.split()
        list_of_highscores.append(tuple(i))
        list_of_scores.append(i[0])
    highscores_file.close()
    for i in range(0, len(list_of_highscores)):
        maximum = list_of_scores.index(max(list_of_scores))
        for i0 in range(0, len(list_of_highscores)):
            if list_of_scores[maximum] == list_of_highscores[i0][0]:
                new_list_of_highscores.append(list_of_highscores.pop(i0))
                break
        list_of_scores.pop(maximum)
    new_list_of_highscores = new_list_of_highscores[:10]
    highscores_file = open(name_of_file, 'w')
    for i in new_list_of_highscores:
        highscores_file.write(i[0] + ' ' + i[1] + '\n')
    highscores_file.close()


while True:
    if condition == 'Main_menu':
        condition, Score = MainMenu()
    if condition == 'Flappy_bird_menu':
        condition, Name = FlappyBirdMenu(Score, Name)
    if condition == 'Flappy_bird_game':
        condition, Score = FlappyBirdGame()
    if condition == 'Highscores_menu':
        condition, Score = HighscoreMenu()

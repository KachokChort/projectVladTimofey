import pygame
import os
import sys


class Resours:
    def __init__(self, resourses):
        self.resourses = resourses



def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size_x = 30
        self.cell_size_y = 30

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color("white"),
                                 (x * self.cell_size_x + self.left, y * self.cell_size_y + self.top,
                                  self.cell_size_x, self.cell_size_y), 1)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size_x, cell_size_y):
        self.left = left
        self.top = top
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

    def get_cell(self, mouse_pos):
        x_click, y_click = mouse_pos
        x_cell = (x_click - self.left) // self.cell_size_x
        y_cell = (y_click - self.top) // self.cell_size_y
        if x_cell < 0 or x_cell >= self.width or y_cell < 0 or y_cell >= self.height:
            return None
        return x_cell, y_cell

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell):
        print(cell)


class Field(Board):
    # создание поля
    def __init__(self, width, height):
        super().__init__(width, height)
        self.board = [[0] * self.width for _ in range(self.height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size_x = 30
        self.cell_size_y = 30

    def get_click(self, mouse_pos, screen, list, props):
        cell = self.get_cell(mouse_pos)
        if cell:
            return self.on_click(cell, screen, list, props)

    def on_click(self, cell, screen, list, props):
        # print(cell)
        # print(bool(self.board[cell[1]][cell[0]]))
        if not bool(self.board[cell[1]][cell[0]]):
            self.board[cell[1]][cell[0]] = 1
            rect = (cell[0] * self.cell_size_x + self.left, cell[1] * self.cell_size_y + self.top, self.cell_size_x,
                    self.cell_size_y)
            rect = pygame.Rect(rect)
            return (Plant(screen, props[0], rect=rect, image=load_image(props[1]), first_image=load_image(props[2]),
                          time=props[3], id=len(list) - 1),
                    cell)
        elif list[cell].set_time():
            resource.resourses[list[cell].name] += 1
            self.board[cell[1]][cell[0]] = 0
            del list[cell]


class Plant:
    def __init__(self, screen, name, rect, time, id, image=None, count=0, first_image=None, FPS=60):
        self.screen = screen
        self.name = name
        self.rect = rect
        self.second_image = image
        self.count = count
        self.time = time
        self.first_image = first_image
        self.image = first_image
        self.isGrow = True
        self.FPS = FPS
        self.id = id

    def set_time(self):
        if self.count // self.FPS >= self.time:
            self.image = self.second_image
            self.isGrow = False
            return True
        return False


class Inventory(Board):
    def __init__(self, width, height, plants):
        super().__init__(width, height)
        self.plants = plants

    def on_click(self, cell):
        try:
            return self.plants[cell[0] + cell[1] * self.width]
        except IndexError:
            pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            return self.on_click(cell)


class Animal_House(Board):
    # создание поля
    def __init__(self, width, height):
        super().__init__(width, height)
        self.board = [[Animal('chiken', 2, 'chiken2.png', first_image='chiken.png') for i in range(self.height)] for _ in
                      range(self.width)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size_x = 30
        self.cell_size_y = 30

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            return self.on_click(cell)

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color("black"),
                                 (x * self.cell_size_x + self.left, y * self.cell_size_y + self.top,
                                  self.cell_size_x, self.cell_size_y), 4)

    def on_click(self, cell):
        ch = self.board[cell[0]][cell[1]]
        if ch.count > ch.time * ch.FPS:
            ch.image = ch.second_image
            ch.count = 0


class Animal:
    def __init__(self, name, time, image=None, count=0, first_image=None, FPS=60):
        self.name = name
        self.second_image = image
        self.count = (time - 1) * FPS
        self.time = time
        self.first_image = first_image
        self.image = first_image
        self.isGrow = True
        self.FPS = FPS

    def set_time(self):
        if self.count // self.FPS >= self.time:
            self.image = self.second_image
            self.isGrow = False
            return True
        return False

resources = {'carrot': 0,'corn': 0,'cucumber': 0,'pumpkin': 0,'sunflower': 0,'tomato': 0,'wheap': 0,'egg': 0}
resource = Resours(resources)
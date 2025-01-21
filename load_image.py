import pygame
import os
import sys
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

    def get_click(self, mouse_pos, screen):
        cell = self.get_cell(mouse_pos)
        if cell:
            return self.on_click(cell, screen)

    def on_click(self, cell, screen):
        #print(cell)
        #print(bool(self.board[cell[1]][cell[0]]))
        if not bool(self.board[cell[1]][cell[0]]):
            self.board[cell[1]][cell[0]] = 1
            rect = (cell[0] * self.cell_size_x + self.left, cell[1] * self.cell_size_y + self.top, self.cell_size_x, self.cell_size_y)
            rect = pygame.Rect(rect)
            return Plant(screen, name='carrot', rect=rect, image=load_image('carrot_1.png'), time=10, first_image=load_image('carrot_2.png'))


class Plant:
    def __init__(self, screen, name, rect, time, image=None, count=0, first_image=None):
        self.screen = screen
        self.name = name
        self.rect = rect
        self. image = image
        self.count = count
        self.time = time
        self.first_image = first_image

class Inventory:
    '''ToDO: сделать запросы для БД вместо txt, нормально обработать вывод инвентаря на компьютер, вывод количества-картинка предметов, показ самого персонажа в инвентаре, показ репутации персонажа в инвентаре, показ инструментов и их урвоень в инвентаре и другие данные '''
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.inventory = pygame.sprite.Sprite()
        self.inventory.image = load_image('inventory.png')
        self.all_sprites.add(self.inventory)
        infoObject = pygame.display.Info()
        dis_x = infoObject.current_w
        dis_y = infoObject.current_h
        screen = pygame.display.set_mode((dis_x, dis_y))
        self.all_sprites.draw(screen)
        self.inventory.rect = self.inventory.image.get_rect()
        self.inventory.rect.x = 100
        self.inventory.rect.y = 150
        with open('inventory_.txt', 'r', encoding='utf-8') as f_in:
            self.inv = f_in.readlines()
        self.inv = str(self.inv[0])
        self.inv = self.inv.split(';')
        self.monets = self.inv[0].split('=')[1]
        self.carrots = self.inv[1].split('=')[1]
        self.wheat = self.inv[2].split('=')[1]
        self.bread = self.inv[3].split('=')[1]
        self.rep = self.inv[4].split('=')[1]
        self.watermelon = self.inv[5].split('=')[1]
        self.potato = self.inv[6].split('=')[1]
        self.dragon_fruit = self.inv[7].split('=')[1]
        self.monets1 = load_image('m0net.png')
        self.all_sprites.add(self.monets1)
        self.monets1.rect = self.monets1.image.get_rect()
        self.monets1.rect.x = 100
        self.monets1.rect.y = 150
        self.carrots1 = load_image('carrots.png')
        self.all_sprites.add(self.carrots1)
        self.carrots1.rect = self.carrots1.image.get_rect()
        self.carrots1.rect.x = 100
        self.carrots1.rect.y = 150
        self.wheat1 = load_image('wheat.png')
        self.all_sprites.add(self.wheat1)
        self.wheat1.rect = self.wheat1.image.get_rect()
        self.wheat1.rect.x = 100
        self.wheat1.rect.y = 150
        self.bread1 = load_image('bread.png')
        self.all_sprites.add(self.bread1)
        self.bread1.rect = self.bread1.image.get_rect()
        self.bread1.rect.x = 100
        self.bread1.rect.y = 150
        self.rep1 = load_image('rep.png')
        self.all_sprites.add(self.rep1)
        self.rep1.rect = self.rep1.image.get_rect()
        self.rep1.rect.x = 100
        self.rep1.rect.y = 150
        self.watermelon1 = load_image('watermelon.png')
        self.all_sprites.add(self.watermelon1)
        self.watermelon1.rect = self.watermelon1.image.get_rect()
        self.watermelon1.rect.x = 100
        self.watermelon1.rect.y = 150
        self.potato1 = load_image('potato.png')
        self.all_sprites.add(self.potato1)
        self.potato1.rect = self.potato1.image.get_rect()
        self.potato1.rect.x = 100
        self.potato1.rect.y = 150
        self.dragon_fruit1 = load_image('dragon_fruit.png')
        self.dragon_fruit1.rect = self.dragon_fruit1.image.get_rect()
        self.dragon_fruit1.rect.x = 100
        self.dragon_fruit1.rect.y = 150
        self.all_sprites.add(self.dragon_fruit1)
        self.dragon_fruit1.draw(screen)



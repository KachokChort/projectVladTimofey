import pygame
import os
import sys

class Farmers:
    # создание поля
    def __init__(self, monets, products):
        #будет БД с хранением информации: количество монет игрока, его продуктами и т.д.


    def sell(self):

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
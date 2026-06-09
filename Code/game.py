#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.const import WIN_WIDTH, WIN_HEIGHT
from Code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        print(pygame.font.get_fonts())
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        print('setup start')
        pygame.init()
        window = pygame.display.set_mode(size=(600, 480))
        print('setup end ')

        print('loop start')
        while True:
            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit() #endgame




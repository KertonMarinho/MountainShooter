#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image




class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/bg.png')
        # retângular para colocar a imagem
        self.rect =self.surf.get_rect(left=0, top=0)

    def run(self, ):
        #a imagem tem que aparecer no retângulo
        self.window.blit(source=self.surf, dest=self.rect)
        #atualiza a tela
        pygame.display.flip()
        pass

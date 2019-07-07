import pygame
from pygame import *
import math
import os
import sys

class Game:

    def __init__(self):
        self.graphics_dir = os.path.join(os.path.dirname('assets'), 'graphics')  
        self.audio_dir = os.path.join(os.path.dirname('assets'), 'audio')
        self.HEIGHT = 640
        self.WIDTH = 480
        self.FPS = 30
        pygame.init()
        pygame.mixer.init()
        self.CANVAS = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Galaga+')

        self.menu()

    def menu(self):
        
        while True:
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

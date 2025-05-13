import pygame
import numpy as np

class cell():
    def __init__(self, colour:tuple=(255, 255, 255), size:int=1, rules:list=[]):
        self.colour = colour
        self.size = size
        self.rules = rules

if __name__ == '__main__':
    
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Cellular Automata")
    
    while True:
        pass

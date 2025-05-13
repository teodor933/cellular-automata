import pygame
import numpy as np


cell_id_tracker = 0


class Rule:
    def __init__(self, cell, push_strength):
        self.cell = cell
        self.push_strength = push_strength


class Cell:
    def __init__(self, colour: tuple = (255, 255, 255), size: int = 1, rules: list = []):
        global cell_id_tracker

        self.id = cell_id_tracker
        self.colour = colour
        self.size = size
        self.rules = rules

        cell_id_tracker += 1


def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Cellular Automata")

    red_cell = Cell(colour=(255, 0, 0), size=5, rules=[
        Rule(0, 1)
    ])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((11, 7, 46))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()

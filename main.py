import pygame
import numpy as np


class Rule:
    def __init__(self, cell, push_strength):
        self.cell = cell
        self.push_strength = push_strength


class Cell:
    def __init__(self, cell_id, colour: tuple = (255, 255, 255), size: int = 1, rules: list = []):
        self.id = cell_id
        self.colour = colour
        self.size = size
        self.rules = rules


class CellFactory:
    def __init__(self):
        self.next_id = 0

    def create_cell(self, colour: tuple = (255, 255, 255), size: int = 1, rules: list = []):
        cell = Cell(self.next_id, colour, size, rules)
        self.next_id += 1
        return cell


def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Cellular Automata")

    factory = CellFactory()
    red_cell = factory.create(colour=(255, 0, 0), size=5, rules=[
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

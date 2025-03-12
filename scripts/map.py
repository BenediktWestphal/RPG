import pygame
import os
#map1 importieren:


class Map:
    def __init__(self, map_file, width=50, height=50):
        self.map_data = self.load_map(map_file)
        self.width = width
        self.height = height
        self.grass = []
        self.walls = []
        
        # self.map_data = [
        #     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # ]

        for row_index, row in enumerate(self.map_data):
            for col_index, tile in enumerate(row):
                if tile == 0:
                    self.grass.append(pygame.Rect(col_index * self.width, row_index * self.height, self.width, self.height))
                elif tile == 1:
                    self.walls.append(pygame.Rect(col_index * self.width, row_index * self.height, self.width, self.height))

    def load_map(self, filename):
        with open(filename, "r") as file:
            return [[int(tile) for tile in line.strip()] for line in file.readlines()]
        


    def draw(self, screen):
        for gras in self.grass:
            pygame.draw.rect(screen, (0, 255, 0), gras)
        for wall in self.walls: 
            pygame.draw.rect(screen, (128, 128, 128), wall)
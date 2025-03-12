import pygame
import sys
from player import *
from map import *
from npc import *
from ui import *
import os


WIDTH, HIGHT = 500, 500

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('RPG GAME')
        self.screen = pygame.display.set_mode((WIDTH, HIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

       # map
        map_path = os.path.join(os.path.dirname(__file__), 'map1.txt')
        self.map = Map(map_path, 50, 50)

        # player
        self.player = Player(x=50, y=50, speed=5)

        # npc
        self.npc = NPC(x=250, y=250, width=50, height=50, color=(255, 255, 0), name="Händler", dialogue="Willkommen! Möchtest du etwas kaufen?")

        # Handelsmenü
        self.trade_menu = TradeMenu(self.screen)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        self.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.handle_movement(keys, self.map.walls, WIDTH, HIGHT)

         # NPC-Interaktion
        if keys[pygame.K_e]:  # Drücke "E" um mit NPC zu sprechen
            message = self.npc.interact(self.player.rect)
            if message:
                print(message)
                self.trade_menu.toggle()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.map.draw(self.screen)
        self.npc.draw(self.screen)
        self.player.draw(self.screen)
        self.trade_menu.draw()
        pygame.display.update()

    def quit(self):
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
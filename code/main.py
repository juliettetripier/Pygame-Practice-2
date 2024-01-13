import pygame
import sys
from settings import width, height, fps, tilesize, world_map
from level import Level
from debug import debug

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Practice 2')
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(fps)

if __name__ == '__main__':
    game = Game()
    game.run()

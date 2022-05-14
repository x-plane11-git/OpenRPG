import pygame, sys
from settings import*

class Game:
    def __init__(self):
    
        #Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.tick.Clock()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                self.screen.fill('black')
                pygame.display.update()
                self.clock.tick(FPS)
if __name__ == '__main__':
    game = Game()
    game.run()
    
import pygame, sys
from setup import*
from level import Level
from pyvidplayer import Video
def intro():
    vid = Video("../media/Game_Intro.mp4")
    vid.set_size((WIDTH,HEIGHT))    
    while True:
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        vid.draw(screen, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.init()
                pygame.mixer.music.load('../audio/click.wav')
                pygame.mixer.music.play()
                vid.close()
                torun()
def torun():
    class Game:
        def __init__(self):
        
            #Initialization
            pygame.init()
            self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
            self.clock = pygame.time.Clock()
            pygame.display.set_caption('OpenRPG')
            
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
                self.clock.tick(FPS)
    if __name__ == '__main__':
        game = Game()
        game.run()
intro()

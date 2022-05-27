import pygame, sys
from setup import*
from level import Level
from pyvidplayer import Video
from tkinter import*
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
splash_screan = Tk()
splash_screan.geometry('700x300+400+300')
splash_screan.overrideredirect(True) # remove border
splash_screan.configure(background='black')
# add text
text = Label(splash_screan, text ="HYPERULT Games", font = ('Arial', 40,'bold'), fg = "white",bg = 'black')
text.place(x = 120, y = 110)
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
def hide():
	splash_screan.destroy()
	intro()
splash_screan.after(5000, hide)

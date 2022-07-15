from setting import *
from controller import Controller

class Ponpoko:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen=pygame.display.set_mode(SCREEN_SIZE)
        self.clock=pygame.time.Clock()
        self.running=True
        self.game_init()
    
    def game_init(self):
        self.controller=Controller(self.screen)
        self.run()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
            
            self.controller.run()
            
            self.clock.tick(FPS)
            pygame.display.update()

Ponpoko()
pygame.quit()
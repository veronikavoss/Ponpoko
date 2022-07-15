from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.frame=0
        self.image=image[self.frame]
        self.rect=self.image.get_rect(topleft=pos)
from email.mime import image
from setting import *

class MapComponent(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect(topleft=pos)
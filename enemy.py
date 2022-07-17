from setting import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image,type,pos):
        super().__init__()
        self.enemy_images=image
        self.enemy_type=type
        self.frame=0
        self.image=self.enemy_images[self.enemy_type][self.frame]
        self.rect=self.image.get_rect(topleft=pos)
from setting import *

class Food(pygame.sprite.Sprite):
    def __init__(self,image,number,index,pos):
        super().__init__()
        self.food_images=image
        self.number=number
        self.food_index=index
        self.image=self.food_images[self.number][self.food_index]
        self.rect=self.image.get_rect(topleft=pos)
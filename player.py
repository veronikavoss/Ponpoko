from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.status='idle'
        self.player_images=image
        self.frame=0
        self.animation_speed=0
        self.image=self.player_images[self.status]
        self.rect=self.image.get_rect(topleft=pos)
        self.direction=self.dx,self.dy=pygame.Vector2(0,0)
        self.move_speed=4
        self.gravity=0.8
        self.front=True
        self.flip=True
        self.on_ground=True
    
    def set_status(self):
        if self.dy<0:
            if self.front:
                self.status='up_down'
                self.animation_speed=0.1
            else:
                self.status='jump'
        elif self.dy>0:
            if self.front:
                self.status='up_down'
                self.animation_speed=0.1
            else:
                self.status='falling'
        else:
            if self.dx!=0:
                self.status='move'
                self.animation_speed=0.1
            else:
                if self.on_ground:
                    if self.front:
                        self.status='idle'
                    else:
                        self.status='stop'
                    self.animation_speed=0
    
    def animate(self):
        animation=self.player_images[self.status]
        print(self.status)
        
        if type(animation)==list:
            self.frame+=self.animation_speed
            if self.frame>=len(animation):
                self.frame=0
            self.image=animation[int(self.frame)]
        else:
            self.image=animation
        self.image=pygame.transform.flip(self.image,self.flip,False)
    
    def set_key_input(self):
        key_input=pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            self.front=False
            self.flip=True
            self.dx=-1
        elif key_input[pygame.K_RIGHT]:
            self.front=False
            self.flip=False
            self.dx=1
        elif key_input[pygame.K_UP]:
            self.front=True
            self.dy=-1
        elif key_input[pygame.K_DOWN]:
            self.front=True
            self.dy=1
        else:
            self.dx=0
            self.dy=0
        
        self.rect.x+=self.dx*self.move_speed
        if self.status=='up_down':
            self.rect.y+=self.dy*self.move_speed
    
    def set_gravity(self):
        pass
    
    def update(self):
        self.set_status()
        self.animate()
        self.set_key_input()
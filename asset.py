from setting import *

class Asset:
    def __init__(self):
        self.sheet_image=pygame.image.load(os.path.join(IMAGE_PATH,'Ponpoko_sheet.png'))
        self.screenshot_image=pygame.image.load(os.path.join(IMAGE_PATH,'ponpoko_screenshot.png'))
        
        self.get_map_component_image()
        self.get_player_image()
        self.get_enemies_image()
        self.get_food_image()
    
    def get_map_component_image(self):
        ground=pygame.Surface((8*SCALE,8*SCALE))
        ground.fill('#00ffff')
        
        border=pygame.Surface((8,8))
        border.blit(self.screenshot_image,(0,0),(0,40,8,8))
        border.set_colorkey('#000000')
        border=pygame.transform.scale(border,(8*SCALE,8*SCALE))
        
        rotated_border=pygame.transform.rotate(border,270)
        
        block=pygame.Surface((8,4))
        block.blit(self.sheet_image,(0,0),(224,216,8,4))
        block.set_colorkey('#292929')
        block=pygame.transform.scale(block,(8*SCALE,4*SCALE))
        
        trap=pygame.Surface((7,7))
        trap.blit(self.sheet_image,(0,0),(144,193,7,7))
        trap.set_colorkey('#292929')
        trap=pygame.transform.scale(trap,(7*SCALE,7*SCALE))
        
        self.tile_image={'ground':ground,'border':border,'rotated_border':rotated_border,'block':block,'ladder':[],'trap':trap}
        
        # ladder
        for x in range(2):
            surface=pygame.Surface((8,8))
            surface.blit(self.sheet_image,(0,0),(x*16+192,216,8,8))
            surface.set_colorkey('#292929')
            surface=pygame.transform.scale(surface,(8*SCALE,8*SCALE))
            self.tile_image['ladder'].append(surface)
    
    def get_player_image(self):
        temp=[]
        
        for y in range(2):
            for x in range(8):
                surface=pygame.Surface((16,16))
                surface.blit(self.sheet_image,(0,0),(x*24,y*24+64,16,16))
                surface.set_colorkey('#292929')
                surface=pygame.transform.scale(surface,(16*SCALE,16*SCALE))
                temp.append(surface)
        
        self.player_images={
            'idle':temp[-1],
            'stop':temp[-7],
            'move':temp[-7:-9:-1],
            'up_down':temp[12:15],
            'jump':temp[10:12]
            }
    
    def get_enemies_image(self):
        temp=[]
        for x in range(8):
            surface=pygame.Surface((16,14))
            surface.blit(self.sheet_image,(0,0),(x*24,113,16,14))
            surface.set_colorkey('#292929')
            surface=pygame.transform.scale(surface,(16*SCALE,14*SCALE))
            temp.append(surface)
        
        self.enemy_images={'enemy1':temp[0:2],'enemy2':temp[2:4],'enemy3':temp[4:6],'enemy4':temp[6:]}
    
    def get_food_image(self):
        self.food_images={'1':[],'2':[],'3':[]}
        
        for y,key in enumerate(self.food_images.keys()):
            if y<2:
                n=8
            else:
                n=6
            for x in range(n):
                surface=pygame.Surface((16,16))
                surface.blit(self.sheet_image,(0,0),(x*24,y*24+136,16,16))
                surface.set_colorkey('#292929')
                surface=pygame.transform.scale(surface,(16*SCALE,16*SCALE))
                self.food_images[key].append(surface)
food_images={'1':[1,2,3],'2':[4,5,6],'3':[7,8,9]}
print(food_images)
for key,value in food_images.items():
    print(key,value)
print('food'+'1'+'-'+'0')
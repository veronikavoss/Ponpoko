from setting import *
from asset import Asset
from map import Map
from map_component import MapComponent
from player import Player

class Controller(Asset,Map):
    def __init__(self,screen):
        Asset.__init__(self)
        self.game_status='playing'
        self.level=1
        Map.__init__(self)
        self.screen=screen
        self.map_load()
        
        # map_editor
        self.map_component=pygame.sprite.Group()
        self.map_element_edit_mode=pygame.sprite.GroupSingle()
        self.player=pygame.sprite.GroupSingle()
        self.map_type='tile'
        self.map_element='ground'
    
    def set_key_input(self):
        key_input=pygame.key.get_pressed()
        if key_input[pygame.K_e] and self.game_status=='playing':
            self.game_status='edit_mode'
            self.player.empty()
            pygame.time.delay(100)
        elif key_input[pygame.K_e] and self.game_status=='edit_mode':
            self.game_status='playing'
            pygame.time.delay(100)
    
    def map_load(self):
        for row_index,column in enumerate(self.map_data[str(self.level)]):
            for column_index,data in enumerate(column):
                x=column_index*MIN_SIZE
                y=row_index*MIN_SIZE
                if data!='_':
                    if data=='player':
                        self.player.add(Player(self.player_images,(x,y)))
                    if data=='ground':
                        self.map_component.add(MapComponent(self.tile_image[data],(x,y)))
                    if data=='border':
                        self.map_component.add(MapComponent(self.tile_image[data],(x,y)))
                    if data=='rotated_border':
                        self.map_component.add(MapComponent(self.tile_image[data],(x,y)))
        print(self.map_data[str(self.level)])
    
    def map_editor(self):
        mouse_pos=pygame.mouse.get_pos()
        row,column=mouse_pos[1]//MIN_SIZE,mouse_pos[0]//MIN_SIZE
        x,y=column*MIN_SIZE,row*MIN_SIZE
        print(row,column,x,y)
        if self.map_element_edit_mode:
            self.map_element_edit_mode.sprite.rect.topleft=(x,y)
        
        self.set_edit_mode_key_input(x,y)
        self.set_edit_mode_mouse_input(row,column,x,y)
        
        for y in range(56):
            for x in range(64):
                pygame.draw.rect(self.screen,'#3c3c3c',(x*MIN_SIZE,y*MIN_SIZE,MIN_SIZE,MIN_SIZE),1)
    
    def set_edit_mode_key_input(self,x,y):
        key_input=pygame.key.get_pressed()
        if key_input[pygame.K_t]:
            self.map_type='tile'
            self.map_element='ground'
            self.map_element_edit_mode.add(MapComponent(self.tile_image[self.map_element],(x,y)))
        elif key_input[pygame.K_p]:
            self.map_type='player'
            self.map_element='player'
            self.map_element_edit_mode.add(Player(self.player_images,(x,y)))
        
        if key_input[pygame.K_1]:
            if self.map_type=='tile':
                self.map_element='ground'
                self.map_element_edit_mode.add(MapComponent(self.tile_image[self.map_element],(x,y)))
            elif self.map_type=='player':
                self.map_element='player'
                self.map_element_edit_mode.add(Player(self.player_images,(x,y)))
        elif key_input[pygame.K_2]:
            if self.map_type=='tile':
                self.map_element='border'
                self.map_element_edit_mode.add(MapComponent(self.tile_image[self.map_element],(x,y)))
        elif key_input[pygame.K_3]:
            if self.map_type=='tile':
                self.map_element='rotated_border'
                self.map_element_edit_mode.add(MapComponent(self.tile_image[self.map_element],(x,y)))
    
    def set_edit_mode_mouse_input(self,row,column):
        mouse_input=pygame.mouse.get_pressed()
        if mouse_input[0]:
            if self.map_data[str(self.level)][row][column]=='_':
                self.map_data[str(self.level)][row][column]=self.map_element
                pygame.time.delay(100)
            elif self.map_data[str(self.level)][row][column]!='_':
                self.map_data[str(self.level)][row][column]='_'
                pygame.time.delay(100)
            self.map_load()
            self.save_map_data()
            # self.reset_map_data()
    
    def reset_map_data(self):
        reset=[['_' for _ in range(SCREEN_WIDTH//MIN_SIZE)] for _ in range(SCREEN_HEIGHT//MIN_SIZE)]
        with open(os.path.join(MAP_PATH,f'map_level-{self.level}.txt'),'w') as w:
            for n1,i in enumerate(reset):
                for n2,j in enumerate(i):
                    if n2<len(i)-1:
                        w.writelines(j+',')
                    else:
                        w.writelines(j)
                if n1<len(reset)-1:
                    w.write('\n')
    
    def save_map_data(self):
        with open(os.path.join(MAP_PATH,f'map_level-{self.level}.txt'),'w') as w:
            for row,column in enumerate(self.map_data[str(self.level)]):
                for index,data in enumerate(column):
                    if index<len(column)-1:
                        w.writelines(data+',')
                    else:
                        w.writelines(data)
                if row<len(self.map_data[str(self.level)])-1:
                    w.write('\n')
    
    def run(self):
        self.screen.fill('black')
        self.set_key_input()
        self.map_component.draw(self.screen)
        self.player.draw(self.screen)
        if self.game_status=='edit_mode':
            self.map_component.draw(self.screen)
            self.player.draw(self.screen)
            self.map_element_edit_mode.draw(self.screen)
            self.map_editor()
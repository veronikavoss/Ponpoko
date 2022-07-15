import pygame,os

SCALE=3
MIN_SIZE=4*SCALE
TITLE='Ponpoko'
SCREEN_SIZE=SCREEN_WIDTH,SCREEN_HEIGHT=MIN_SIZE*64,MIN_SIZE*56 # 256,224
FPS=60

CURRENT_PATH=os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH=os.path.join(CURRENT_PATH,'image')
MAP_PATH=os.path.join(CURRENT_PATH,'map')
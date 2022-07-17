from setting import *

class Map:
    def __init__(self):
        self.map_data={
            str(self.level):[]
        }
        with open(os.path.join(MAP_PATH,f'map_level-{self.level}.txt'),'r') as r:
            for data in r.readlines():
                self.map_data[str(self.level)].append(data.strip().split(','))
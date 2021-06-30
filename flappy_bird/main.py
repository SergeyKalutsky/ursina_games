from random import randint
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()
bg = Entity(model='quad', scale_y=1.8, texture='background')
left_black = Entity(model='quad', 
                    scale_y=9, 
                    scale_x=5.1,
                    color=color.black,
                    x=-5, z=-.5)
bg.scale *= 5.0


class Pipe(Entity):
    def __init__(self):
        super().__init__(self, model='quad',
                         scale_y=4.5, 
                         texture='pipe', 
                         z=-.2, y=-randint(2, 5), x=2.1)
    
    def update(self):
        self.x -= 0.02
        if self.x < -4:
            self.x = 2.1
            self.y = -randint(2, 5)


def update_player():
    if held_keys['space']:
        player.y += 0.15
    player.y -= 0.05


player = PlatformerController2d(texture='bird',
                                model='quad', scale=0.8,
                                z=-1, x=-1.9)
Pipe()

player.update = update_player
app.run()

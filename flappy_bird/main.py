from ursina import *
from random import randint
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()
bg = Entity(model='quad', scale_y=1.8, texture='background')
lb = Entity(model='quad',
            scale_y=9,
            scale_x=5.1,
            color=color.black,
            x=-5, z=-.5)
rb = Entity(model='quad',
            scale_y=9,
            scale_x=5.1,
            color=color.black,
            x=4.9, z=-.5)
bg.scale *= 5.0

class GameState(Entity):
    on = True

class Pipe(Entity):
    def __init__(self, rotate=False):
        super().__init__(self, model='quad',
                         scale_y=4.5,
                         texture='pipe',
                         z=-.2,
                         collider='box')
        self.rotate = rotate
        self.y = -randint(2, 5)
        self.x = randint(3, 5)
        if self.rotate:
            self.rotation_z = 180
            self.y *= -1


    def update(self):
        if game.on:
            self.x -= 0.02
            if self.x < -4:
                self.x = randint(3, 5)
                self.y = -randint(2, 5)
                if self.rotate:
                    self.rotation_z = 180
                    self.y *= -1


def update_player():
    if game.on:
        if held_keys['space']:
            player.y += 0.15
        player.y -= 0.05


player = PlatformerController2d(texture='bird',
                                model='quad', scale=0.8,
                                z=-.2, x=-1.9, collider='box')
p1 = Pipe()
p2 = Pipe(rotate=True)
game = GameState()
EditorCamera()

def update():
    if player.intersects(p1).hit or player.intersects(p2).hit:
        game.on = False
    if not game.on:
        Text(text='GAME OVER', scale=3, origin=(0, 0), color=color.red)
        

player.update = update_player
app.run()

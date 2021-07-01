import os
from subprocess import check_call
from ursina import *


app = Ursina()
EditorCamera()


class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__(model='sphere', x=x, y=y,
                         scale=0.3, color=color.rgb(235, 159, 54))

    def update(self):
        self.z += 1
        if self.z > 200:
            destroy(self)


class SpaceShip(Entity):
    def __init__(self):
        super().__init__(model='assets/StarSparrow01')
        # cooldown
        self.cooldown = 0
        self.cooldown_limit = 0.5
        # textures
        self.tecture_indx = 0
        self.textures = [f.split('.')[0] for f in os.listdir('textures')]
        self.texture = self.textures[self.tecture_indx]


    def update(self):
        if held_keys['d']:
            self.x += 0.2
            self.rotation_z += 0.2
        if held_keys['a']:
            self.x -= 0.2
            self.rotation_z -= 0.2
        if held_keys['space']:
            if not self.cooldown > 0:
                Bullet(self.x, self.y)
                self.cooldown = self.cooldown_limit
        if self.cooldown > 0:
            self.cooldown -= time.dt

def change_color():
    ship.tecture_indx += 1
    ship.texture = ship.textures[ship.tecture_indx % len(ship.textures)] 


b = Button(color=color.gray, icon='assets/color_picker', scale=.1, x=0.7, y=0.4)
b.on_click = change_color
ship = SpaceShip()

app.run()

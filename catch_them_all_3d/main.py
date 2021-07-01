from random import randint
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.exit_button.visible = True


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            color=color.random_color(),
            alpha=0.5
        )


class Enemy(Entity):
    def __init__(self):
        super().__init__(model='sphere',
                         collider='box',
                         position=(randint(0, 9),
                                   randint(1, 3),
                                   randint(20, 40)))
        self.main_color = color.random_color()
        self.count = 0
        self.color = self.main_color

    def reset_color(self):
        if self.color != self.main_color and self.count <= 0:
            self.color = self.main_color
        if self.count > 0:
            self.count -= 1

    def update(self):
        self.z -= 0.2
        self.reset_color()
        if self.z <= 0:
            self.z = randint(20, 40)

    def on_click(self):
        self.color = color.red
        self.count = 2
        if self.z < 7:
            self.z = randint(30, 40)
            self.main_color = color.random_color()
            self.color = self.main_color
            score.text = str(int(score.text)+1)


player = FirstPersonController()
score = Text(text='1', y=.43, x=-.75, scale=1.5, origin=(0, 0), background=True)

for i in range(5):
    Enemy()

for z in range(100):
    for x in range(10):
        Voxel(position=(x, 0, z))


def update():
    if player.x >= 9:
        player.x = 9
    if player.x <= 1:
        player.x = 1
    if player.z != 0:
        player.z = 0


app.run()

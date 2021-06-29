from ursina import *

app = Ursina()
window.exit_button.visible = True


def get_color(x, y):
    if x % 2 == 0:
        return color.white if y % 2 == 0 else color.gray
    return color.gray if y % 2 == 0 else color.white


class BoardSquere(Entity):
    def __init__(self, x, z, scale=(1.3, 0.2, 1.3)):
        super().__init__(
            model='cube',
            scale=scale,
            color=get_color(x, z),
            position=(x*scale[0], 0, z*scale[2])
        )
        self.x = x*scale[0]
        self.z = z*scale[2]


def make_board():
    for z in range(8):
        for x in range(8):
            BoardSquere(x, z)


Entity(model='assets/checker',
       color=color.black,
       scale=0.4,
       position=(0, 0.2, 0))

Entity(model='assets/checker',
       color=color.white,
       scale=0.4,
       position=(1.3, 0.2, 0))

EditorCamera()
make_board()
app.run()

from ursina import *

app = Ursina()
window.exit_button.visible = True


def get_color(x, y):
    if x % 2 == 0:
        return color.white if y % 2 == 0 else color.gray
    return color.gray if y % 2 == 0 else color.white


class GameState(Entity):
    selected_checker = None


class Checker(Entity):
    def __init__(self, x, z, color):
        super().__init__(
            model='assets/checker',
            scale=0.4,
            position=(x*1.3, 0.2, z*1.3),
            color=color,
            collider='box'
        )
        self.main_color = color
        self.selected = False

    def update(self):
        if not self.selected and self.color != self.main_color:
            self.color = self.main_color

    def on_click(self):
        self.color = color.green
        game.selected_checker = self
        self.selected = True

    def on_double_click(self):
        destroy(self)


class BoardSquere(Entity):
    def __init__(self, x, z, c, scale=(1.3, 0.2, 1.3), checker=None):
        super().__init__(
            model='cube',
            scale=scale,
            collider='box',
            color=c,
            position=(x*scale[0], 0, z*scale[2])
        )
        self._x = x
        self._z = z
        self.checker = checker

    def on_click(self):
        if game.selected_checker:
            self.checker = game.selected_checker
            self.checker.x = self._x * 1.3
            self.checker.z = self._z * 1.3
            self.checker.selected = False
            game.selected_checker = None


def make_board():
    for z in range(8):
        for x in range(8):
            c = get_color(x, z)
            if z in (0, 1, 2) and c == color.gray:
                BoardSquere(x, z, c, checker=Checker(x, z, color.black))
            elif z in (5, 6, 7) and c == color.gray:
                BoardSquere(x, z, c, checker=Checker(x, z, color.white))
            else:
                BoardSquere(x, z, c)


game = GameState()
EditorCamera()
make_board()
app.run()

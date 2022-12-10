class CRT:
    def __init__(self):
        self.sprite = [0, 1, 2]
        self.cursor = 0
        self.screen = ''

    def set_sprite(self, x):
        self.sprite = [x-1, x, x+1]

    def tick(self):
        self.draw_pixel()

        self.cursor += 1
        if self.cursor == 40:
            self.cursor = 0
            self.screen += '\n'

    def draw_pixel(self):
        pixel = '.'
        if self.cursor in self.sprite:
            pixel = '#'

        self.screen += pixel





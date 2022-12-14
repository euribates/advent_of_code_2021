from functools import partial
import random

from PIL import Image, ImageDraw

from vectors import Vector2

RED = (255, 99, 99)
GREEN = (99, 255, 99)

SCALE = 25

class Grid:
    
    def __init__(self, width, height, scale=SCALE):
        self.scale = SCALE
        self.width = width * self.scale
        self.height = height * self.scale
        self.center = Vector2(self.width // 2, self.height // 2)
        self.size = (self.width, self.height)
        self.img = Image.new('RGBA', self.size, (0, 0, 0, 255))
        self.axis()
        
    def transform(self, point: Vector2) -> (int, int):
        x = self.center.x + point.x * self.scale
        y = self.center.y - point.y * self.scale
        return x, y
        
    def axis(self):
        draw = ImageDraw.Draw(self.img)
        draw.line(
            (self.center.x, 0, self.center.x, self.height),
            fill=128,
        )
        draw.line(
            (0, self.center.y, self.width, self.center.y),
            fill=128,
        )
    
    def dot(self, point, color=GREEN):
        x = self.center.x + point.x * self.scale
        y = self.center.y - point.y * self.scale
        offset = self.scale // 5
        box = (x - offset, y - offset, x + offset, y + offset)
        draw = ImageDraw.Draw(self.img)
        draw.ellipse(box, fill=color)

    def box(self, point, color=RED):
        x = self.center.x + point.x * self.scale
        y = self.center.y - point.y * self.scale
        offset = self.scale // 5
        box = (x - offset, y - offset, x + offset, y + offset)
        draw = ImageDraw.Draw(self.img)
        draw.rounded_rectangle(box, radius=2, fill=color)

    def show(self):
        self.img.show()
        
        
if __name__ == '__main__':
    g = Grid(11, 11)
    g.box(Vector2(0, 0))
    g.dot(Vector2(2, 3))
    g.show()



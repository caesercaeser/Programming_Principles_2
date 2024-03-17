import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        
p1=input()
p2=input()
point=Point(p1,p2)
print(point.show())
print(point.move(int(input()), int(input())))
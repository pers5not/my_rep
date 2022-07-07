import re


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceForOrigin(self):
        return((self.x ** 2) + (self.y ** 2) * 0.5)

    def halway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(int(mx), int(my))

    def __str__(self) -> str:
        return f"Point (x = {self.x} y = {self.y})"


p1 = Point(3, 5)
p2 = Point(7, 9)
mid = p1.halway(p2)
print(mid)
print(mid.getX())
print(mid.getY())

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def getX(self):
        return self.x


point_a = Point(5, 10)
point_b = Point(7, 14)

print(f"{point_a.getX()}\n{point_b.getX()}")

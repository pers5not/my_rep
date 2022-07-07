class Point:
    def __init__(self, initX, initY) -> None:
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceForOrigin(self):
        return((self.x ** 2) + (self.y ** 2) * 0.5)

    def __str__(self) -> str:
        return f"Point ({self.x}; {self.y})"


p = Point(7, 6)
p2 = Point(9, 10)
print(f"{p}\n{p2}")

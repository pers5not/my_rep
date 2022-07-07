class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point ({self.x} {self.y})"

    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x,
                     self.y + otherPoint.y)

    def __sub__(self, otherPoint):
        return Point(self.x - otherPoint.x,
                     self.y - otherPoint.y)


p1 = Point(-1, 5)
p2 = Point(15, 20)

print(f"{p1}\n{p2}\n")
print(p1 + p2)
print(p1 - p2)

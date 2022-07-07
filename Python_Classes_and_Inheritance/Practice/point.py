class Point():
    def getX(self):
        return self.x


point1 = Point()
point2 = Point()

print(point1)

# переменные экземпляра
point1.x = 10
point2.x = 20
print(f"{point1.getX()}")

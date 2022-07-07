from ntpath import join


class Point:
    printed_rep = '*'

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y) + 2)
        for j in range(size - 1):
            if (j + 1) == int(self.y):
                special_row = str((j+1) % 10) + \
                    (" "*(int(self.x) - 1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j + 1) % 10))
        rows.reverse()
        x_axis = ''

        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return '\n'.join(rows)


p1 = Point(3, 3)
p2 = Point(5, 8)

print(p1.graph())
print()
print(p2.graph())

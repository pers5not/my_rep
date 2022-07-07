class Fruit():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def sort_priorit(self):
        return self.price


L = [
    Fruit('Cheri', 120),
    Fruit('Banan', 15),
    Fruit('Orange', 20)
]

# for f in sorted(L, key=Fruit.sort_priorit):
#     print(f.price, f.name)
'''ОДНО И ТОЖЕ'''
# ===========================================
for f in sorted(L, key=lambda x: x.sort_priorit()):
    print(f.price, f.name)

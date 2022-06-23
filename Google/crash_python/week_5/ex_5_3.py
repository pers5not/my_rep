# У нас есть два предмета мебели: коричневый деревянный стол и красный кожаный диван. Заполните пробелы после создания каждого экземпляра класса Furniture, чтобы функция description_furniture могла отформатировать предложение, описывающее эти предметы, следующим образом: «Этот предмет мебели сделан из {цвета} {материала}».
class Furniture:
    color = ""
    material = ""


table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"


def describe_furniture(piece):
    return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))


print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"

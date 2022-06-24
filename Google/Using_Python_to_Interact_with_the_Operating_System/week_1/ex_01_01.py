from PIL import Image
import random
import pandas
image = Image.open(
    "Using_Python_to_Interact_with_the_Operating_System/week_1/av_8.png")
print(image.size)
print(image.format)
visitors = [random.randint(1111, 5555) for i in range(5)]
errors = [random.randint(11, 100) for i in range(5)]
df = pandas.DataFrame(
    {'visitors': visitors, 'errors': errors}, index=['Mon', 'Tues', 'Wed', 'Thu', 'Fri'])

print(df)

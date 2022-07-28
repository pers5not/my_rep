from PIL import Image
import requests
from io import BytesIO

response = requests.get("https://stenson.com.ua/img.php?id=18161&size=3")
img = Image.open(BytesIO(response.content))

# img.show()
print(img)
img.save('1.png')
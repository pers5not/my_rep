import xml.etree.ElementTree as ET

data = """<person> 
<name>Alex</name>
<phone type="intl">
+38 095 376 7993
</phone>
<email hide="yes"/>
</person>
"""

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

import xml.etree.ElementTree as ET

data = """<stuff>
<users>
    <user x="2">
        <name>Alex</name>
        <id>1</id>
    </user>
    <user x="3">
        <name>Mihail</name>
        <id>2</id>
    </user>
</users>
</stuff>
"""
tree = ET.fromstring(data)
lst = tree.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attr:', item.get('x'))

import xml.etree.ElementTree as ET

line = '''<person>
<name>Sergey</name>
</person>'''
tree = ET.fromstring(line)
print("Text:", tree.find('name').text)
print(type(tree))

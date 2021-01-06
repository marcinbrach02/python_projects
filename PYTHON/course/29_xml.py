import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
data = tree.getroot()

for child in data:
    print(child.tag)
    print(child.attrib)
    print(child.text)

print(data[0][1].tag)
print(data[0][1].text)


for fname in data.iter('fname'):
    print(fname.text)

#findall, zawsze zbiór, find pierwszy element
user = data.find("./user[@id='2']/fname")
print(user)

new_user = ET.Element('user')
new_user.set('id', '3')
data.append(new_user)

fname = ET.SubElement(new_user, 'fname')
fname.text = 'Kolejne'
ET.SubElement(new_user, 'lname').text = 'Nazwisko'

print(ET.tostring(data))
tree.write('data.xml', encoding='utf-8')





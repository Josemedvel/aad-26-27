from lxml import etree

tree = etree.parse("personas.xml")
root = tree.getroot()

# para ver la etiqueta en sí
print(root.tag)
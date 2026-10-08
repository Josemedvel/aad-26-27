from lxml import etree

tree = etree.parse("personas.xml")
root = tree.getroot()

primera_persona = root.find("persona")
print(primera_persona)
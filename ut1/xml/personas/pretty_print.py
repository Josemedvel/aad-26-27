from lxml import etree

def prettyprint(element):
    xml = etree.tostring(element, pretty_print=True)
    print(xml.decode(), end="")

tree = etree.parse("personas.xml")
root = tree.getroot()

prettyprint(root)
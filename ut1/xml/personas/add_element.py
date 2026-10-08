from lxml import etree

def prettyprint(element):
    xml = etree.tostring(element, pretty_print=True)
    print(xml.decode(), end="")

tree = etree.parse("personas.xml")
root = tree.getroot()

primera_persona = root.find("persona")
# comprobamos que sea un elemento
if etree.iselement(primera_persona):
    # comprobamos que la etiqueta tenga hijos
    if len(primera_persona):
        print("La etiqueta tiene hijos")
        for hijo in primera_persona:
            print(hijo)
    # creamos una nueva etiqueta
    direccion = etree.Element("direccion")
    direccion.text = "c/ Madrid 32, Getafe, 28905"
    primera_persona.append(direccion)
prettyprint(root)
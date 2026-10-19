from lxml import etree
from pathlib import Path

def prettyprint(element):
    xml = etree.tostring(element, pretty_print=True)
    print(xml.decode(), end="")

# remove_blank_text elimina los espacios/saltos del fichero original para que
# pretty_print pueda reindentar todo, incluido el elemento nuevo
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(Path(__file__).parent / "personas.xml", parser)
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
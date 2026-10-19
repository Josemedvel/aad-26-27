from lxml import etree
from pathlib import Path

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(Path(__file__).parent / "personas.xml", parser)
root = tree.getroot()

primera_persona = root.find("persona")
if etree.iselement(primera_persona):
    # SubElement crea la etiqueta y la añade al padre en un solo paso
    direccion = etree.SubElement(primera_persona, "direccion")
    direccion.text = "c/ Madrid 32, Getafe, 28905"

    # también admite atributos como argumentos con nombre
    telefono = etree.SubElement(primera_persona, "telefono", tipo="movil")
    telefono.text = "600123456"

print(etree.tostring(root, pretty_print=True).decode(), end="")

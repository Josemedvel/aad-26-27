from lxml import etree
from pathlib import Path

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(Path(__file__).parent / "personas.xml", parser)
root = tree.getroot()

persona = root.find("persona[@id='1']")
if persona is not None:
    # cambiar el texto de un elemento
    nombre = persona.find("nombre")
    print("Antes:", nombre.text)
    nombre.text = "Ana María"

    # el contenido es siempre texto: convertimos para operar y volvemos a str
    edad = persona.find("edad")
    edad.text = str(int(edad.text) + 1)

print(etree.tostring(root, pretty_print=True, encoding="unicode"), end="")

# para guardar los cambios en el fichero:
# tree.write("personas.xml", pretty_print=True, encoding="UTF-8", xml_declaration=True)

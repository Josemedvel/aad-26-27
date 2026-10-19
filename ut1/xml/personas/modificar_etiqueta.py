from lxml import etree
from pathlib import Path

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(Path(__file__).parent / "personas.xml", parser)
root = tree.getroot()

persona = root.find("persona")
if persona is not None:
    # la etiqueta se cambia asignando a .tag
    print("Antes:", persona.tag)
    persona.tag = "usuario"
    print("Después:", persona.tag)

    # renombrar un hijo
    persona.find("edad").tag = "anios"

# renombrar todas las etiquetas "nombre" del documento
for nombre in root.iter("nombre"):
    nombre.tag = "nombre_completo"

print(etree.tostring(root, pretty_print=True, encoding="unicode"), end="")

# para guardar los cambios en el fichero:
# tree.write("personas.xml", pretty_print=True, encoding="UTF-8", xml_declaration=True)

from lxml import etree
from pathlib import Path

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(Path(__file__).parent / "personas.xml", parser)
root = tree.getroot()

# eliminar un hijo: se llama a remove desde el padre
persona = root.find("persona[@id='1']")
if persona is not None:
    edad = persona.find("edad")
    if edad is not None:
        persona.remove(edad)

# eliminar sin conocer el padre: getparent() (propio de lxml)
for p in root.findall("persona[@activo='false']"):
    p.getparent().remove(p)

print(etree.tostring(root, pretty_print=True, encoding="unicode"), end="")

# para guardar los cambios en el fichero:
# tree.write("personas.xml", pretty_print=True, encoding="UTF-8", xml_declaration=True)

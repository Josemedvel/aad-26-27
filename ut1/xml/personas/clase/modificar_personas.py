from lxml import etree
from pathlib import Path

def pretty_print(elemento):
    xml = etree.tostring(elemento, pretty_print = True)
    print(xml.decode(), end="")

p = Path(__file__).parent.parent / "personas.xml"
p_out = Path(__file__).parent.parent / "personas_mod.xml"
print(p)

tree = etree.parse(p)
root = tree.getroot()

if etree.iselement(root):
    pretty_print(root)
    
nueva_persona = etree.SubElement(root, "persona", id="3", activo="true")
nuevo_nombre = etree.SubElement(nueva_persona, "nombre")
nuevo_nombre.text = "Carlos"
nueva_edad = etree.SubElement(nueva_persona, "edad")
nueva_edad.text = "67"
pretty_print(root)

tree.write(p_out, encoding="UTF-8", pretty_print=True, xml_declaration=True)






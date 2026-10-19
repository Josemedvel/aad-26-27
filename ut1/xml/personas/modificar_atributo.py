from lxml import etree
from pathlib import Path

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(Path(__file__).parent / "personas.xml", parser)
root = tree.getroot()

persona = root.find("persona[@id='2']")
if persona is not None:
    print("Antes:", persona.get("activo"))
    # set sobreescribe el valor si el atributo existe (y lo crea si no)
    persona.set("activo", "true")

    # alternativa como diccionario
    persona.attrib["id"] = "20"

    # los valores de atributos siempre son str
    print("Después:", persona.get("activo"), persona.get("id"))

    # borrar un atributo (del lanza KeyError si no existe)
    del persona.attrib["id"]
    # alternativa que no falla si no existe:
    persona.attrib.pop("activo", None)
    print("Atributos tras borrar:", persona.keys())

print(etree.tostring(root, pretty_print=True, encoding="unicode"), end="")

# para guardar los cambios en el fichero:
# tree.write("personas.xml", pretty_print=True, encoding="UTF-8", xml_declaration=True)
